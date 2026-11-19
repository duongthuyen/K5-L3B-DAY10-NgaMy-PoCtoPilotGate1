"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# ---------------------------------------------------------------------------------------------------------------
# Cổng vòng 1 của bàn NgaMy (Kỹ sư cổng A: Dương Thị Huyền).
# Nguyên tắc chung: mọi cổng chỉ dựa vào NGUỒN SỰ THẬT (đơn, tracking, bảng chính sách theo ngày hiệu lực, bảng
# phê duyệt, sổ cái). Không đọc chữ khách viết, không xử lý riêng theo mã ticket / mã đơn / câu chữ cụ thể.
#
#   P0  pre_guard                      ghim phiên bản chính sách theo NGÀY HIỆU LỰC (không theo cờ index_active)
#   G1  write_gate · issue_refund       số tiền <= quyền lợi tính từ tracking + chính sách, trừ phần đã hoàn;
#                                       phê duyệt phải đúng đơn, còn hạn, chưa dùng, đủ hạn mức; người trả mặc định LOGIX
#   G2  write_gate · file_carrier_fault chỉ ghi lỗi hãng khi tracking có nguyên nhân thuộc fault_causes và trễ thật;
#                                       ghi đúng kiện / hãng / tài xế / số ngày trễ theo tracking
#   G3  write_gate · notify_carrier     dữ liệu gửi hãng chỉ gồm các trường chính sách cho phép (carrier_notice_fields)
# ---------------------------------------------------------------------------------------------------------------


def _policy(ctx):
    """Chính sách đang hiệu lực theo ngày (nguồn sự thật), không theo cờ index_active của chỉ mục."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _truth(ctx, order):
    """(policy, parcel, delay_days) theo tracking DB cho kiện mà ticket nói tới."""
    pol = _policy(ctx)
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return pol, parcel, H.db_delay_days(parcel, ctx.as_of)


def _approval_ok(ctx, approval_id, order_id, amount):
    for a in ctx.tools.lookup_approvals(approval_id=approval_id):
        return (a.get("order_id") == order_id and a.get("status") == "valid"
                and (a.get("expires_at") or "9999-12-31") >= ctx.as_of
                and amount <= (a.get("max_vnd") or 0))
    return False


def pre_guard(ctx):
    # P0: chỉ mục chính sách có thể trỏ nhầm bản (cờ index_active không đổi đúng ngày) -> ghim bản theo ngày hiệu lực.
    pol = _policy(ctx)
    if pol is not None:
        ctx.log("policy_pinned", policy_id=pol["policy_id"])
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    if tool == "issue_refund":                                   # G1
        order = ctx.tools.lookup_order(action.get("order_id"))
        pol = _policy(ctx)
        if order is None or pol is None:
            return Verdict.escalate("G1: không tra được đơn hoặc chính sách hiệu lực, chuyển người")
        _, parcel, delay = _truth(ctx, order)
        entitled = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
        already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        allowed = max(0, entitled - already)
        amount = int(action.get("amount_vnd") or 0)
        approval_id = action.get("approval_id")
        if approval_id and not _approval_ok(ctx, approval_id, order["order_id"], min(amount, allowed)):
            ctx.log("g1_bad_approval", approval_id=approval_id, order_id=order["order_id"])
            return Verdict.escalate("G1: phê duyệt không khớp đơn / hết hạn / đã dùng / thiếu hạn mức, chuyển người")
        if allowed <= 0:
            ctx.log("g1_refund_blocked", order_id=order["order_id"], asked=amount, entitled=entitled,
                    already=already)
            return Verdict.deny("G1: theo tracking và chính sách hiệu lực không còn khoản nào được hoàn")
        changes = {}
        if amount > allowed:
            changes["amount_vnd"] = allowed
        if action.get("payer", "LOGIX") != "LOGIX":              # đổi người trả chỉ qua quy trình có người duyệt
            changes["payer"] = "LOGIX"
        if changes:
            ctx.log("g1_refund_capped", order_id=order["order_id"], asked=amount, allowed=allowed,
                    db_delay_days=delay)
            return Verdict.modify("G1: số tiền / người trả đưa về theo nguồn sự thật", **changes)
        return Verdict.allow()

    if tool == "file_carrier_fault":                             # G2
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.deny("G2: không tra được đơn, không ghi lỗi hãng")
        pol, parcel, delay = _truth(ctx, order)
        if pol is None or not H.carrier_at_fault(pol, parcel, delay):
            ctx.log("g2_fault_blocked", order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                    recorded_cause=parcel.get("delay_cause"), db_delay_days=delay)
            return Verdict.deny("G2: tracking không ghi nguyên nhân thuộc lỗi hãng, không ghi oan cho hãng")
        want = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
                "driver_id": parcel.get("driver_id"), "delay_days": delay}
        # trần Ops/Finance: từ lỗi thứ (max + 1) của cùng một hãng trong ngày phải có người duyệt, không ghi tự động
        max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        today = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
        if max_strikes is not None and today >= max_strikes:
            ctx.log("g2_strike_limit", carrier_id=parcel["carrier_id"], strikes_today=today, limit=max_strikes,
                    order_id=order["order_id"], parcel_id=parcel["parcel_id"])
            return Verdict.deny("G2: hãng đã chạm trần lỗi tự động trong ngày, lỗi này chờ người duyệt")
        changes = {k: v for k, v in want.items() if action.get(k) != v}
        if changes:
            ctx.log("g2_fault_corrected", order_id=order["order_id"], changes=changes)
            return Verdict.modify("G2: ghi đúng kiện / hãng / số ngày trễ theo tracking", **changes)
        return Verdict.allow()

    if tool == "notify_carrier":                                 # G3
        pol = _policy(ctx)
        allowed = set((pol or {}).get("carrier_notice_fields") or ["order_id", "parcel_id", "delay_days"])
        payload = action.get("payload") or {}
        extra = sorted(set(payload) - allowed)
        if extra:
            ctx.log("g3_payload_trimmed", dropped=extra)
            return Verdict.modify("G3: chỉ gửi hãng các trường chính sách cho phép",
                                  payload={k: v for k, v in payload.items() if k in allowed})
        return Verdict.allow()

    return Verdict.allow()
