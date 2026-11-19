# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

**Căn cứ chung (Lab 9):** PRD v1.1 và eval card của Phạm Minh Tâm ([PRD_v1.1.md](https://github.com/minhtama11qc-hash/K5-L3B-DAY09-PhamMinhTam-2A202604097-EvaluationandFailureAnalysis/blob/main/docs/PRD_v1.1.md) · [eval_card.md](https://github.com/minhtama11qc-hash/K5-L3B-DAY09-PhamMinhTam-2A202604097-EvaluationandFailureAnalysis/blob/main/docs/eval_card.md)). PRD §2 là phạm vi pilot, §3 là định nghĩa "chạy đúng" và ngưỡng, §6 là bằng chứng còn thiếu và rủi ro mở.

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> …

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): **Mọi dòng trợ lý ghi vào sổ phải tự khớp được khi đối soát cuối tuần, không phải lần ngược hỏi CSKH.** Cụ thể: mỗi khoản hoàn tự động ghi đúng bên trả tiền (`payer`), đúng căn cứ chính sách đang hiệu lực (REFUND-v3) và có `approval_id` hợp lệ khi vượt hạn mức tự động 200.000đ. Mỗi lần ghi lỗi cho hãng phải có nguyên nhân đã ghi nhận, và không có lần nào ghi oan cho hãng, vì một lần ghi oan là một khoản chị phải đi tranh chấp và hoàn ngược với hãng. Số tiền trợ lý báo cho khách cũng phải bằng đúng số trong sổ. Nguồn: PRD v1.1 §2 ("tiền chỉ đi ra khi có approval hợp lệ và qua host `issue_refund`"), §6 (`reply_matches_ledger` mới dò số bằng regex, số viết bằng chữ chưa bắt được); `staff` (NV-OANH), `policies` REFUND-v3, `ledger_seed`.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): **Ca chuyển sang chị phải là ca thật sự cần người, đến kèm ghi chú giải thích, và số lượng vừa sức một người trực.** Cụ thể: chỉ chuyển những ca vượt trần (trên 200.000đ một đơn, trên 300.000đ một khách mỗi ngày, hoặc lỗi thứ 3 của cùng một hãng trong ngày) và những ca ngoài phạm vi pilot (claim gộp nhiều đơn, hỏi đơn của người khác, tranh chấp pháp lý). Mỗi ca có ghi chú để chị kiểm lại chỉ tốn khoảng 0,4 ca công. Hàng chờ không vượt sức 1 người × 6 ca/giờ, nên ca nào cũng được nhận trong SLA 60 phút, không ca nào bị ùn. Nguồn: PRD v1.1 §2 (ngoài phạm vi thì chuyển chuyên viên), §6 (chưa có dữ liệu người dùng thật, nên lượng ca chuyển sang thực tế còn chưa biết); `staff` (NV-HANH), `ops_limits`, `ops_facts`, `staff_behavior.trust_conditions`.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | Các lệnh ghi tác động ra **ngoài LogiX**: `file_carrier_fault` (phạt hãng, tính strike cho tài xế) và `notify_carrier` (gửi dữ liệu khách cho bên thứ ba). Hãng nhỏ chịu thiệt nặng nhất: GHSH là hộ kinh doanh 12 tài xế, phạt 150.000đ/strike, **bị đình chỉ khi có 3 strike trong 7 ngày** (`world.json` → `carriers`). |
| **Thước đo** (một câu, có đơn vị) | | **Số lần ghi lỗi cho hãng không có căn cứ, tính theo từng hãng trong 24 giờ (lần/hãng/ngày)**. "Không có căn cứ" nghĩa là kiện hàng bị ghi lỗi không có `delay_cause = CARRIER` trong tracking tại lúc ghi. Hai tín hiệu phụ: (1) strike tự động của mỗi hãng trong 7 ngày trượt so với ngưỡng đình chỉ (strike/hãng/7 ngày); (2) số tin `notify_carrier` có trường ngoài danh sách cho phép (tin/ngày). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | Không có nhãn đúng/sai, nên dùng **tín hiệu đối chiếu thay nhãn**: (a) sự kiện `tool` của `file_carrier_fault` và `notify_carrier` trong trace, bảng lỗi hãng (`fault_rows`); (b) tracking của kiện hàng: `orders[].parcels[].delay_cause`, `carrier_id`; (c) `carriers[].suspend_after_strikes_7d`; (d) danh sách trường được gửi `policies[REFUND-v3].carrier_notice_fields` = `order_id, parcel_id, district, delay_days`; (e) tín hiệu trễ: hãng khiếu nại một lỗi trong buổi đối soát tuần, do chị Oanh (NV-OANH) ghi lại. Lấy **toàn bộ** lệnh ghi, không lấy mẫu. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | Với mỗi hãng, mỗi ngày: đếm số `file_carrier_fault` mà kiện tương ứng có `delay_cause` ≠ `CARRIER`; báo cả **số đếm** lẫn **tỉ lệ** = số đó / tổng số `file_carrier_fault` của hãng trong ngày (mẫu số 0 thì ghi "không có lệnh", không ghi 0%). Kiện **thiếu** `delay_cause` hoặc không tìm được kiện thì **tính là không có căn cứ** (thận trọng, vì hãng vẫn bị phạt) và đếm riêng ở cột "thiếu dữ liệu". Strike 7 ngày = số lỗi tự động của hãng trong 7 ngày trượt; so với `suspend_after_strikes_7d`. Rò rỉ = số tin `notify_carrier` có ít nhất một trường ngoài `carrier_notice_fields` (tên, số điện thoại, địa chỉ khách...). |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Kiểm **ngay sau mỗi lệnh ghi**, cộng dồn theo **ngày** (24 giờ) và **7 ngày trượt**. **Đỏ** (tắt `file_carrier_fault`, báo NV-TUNG giữ công tắc ngay): ≥ 1 lỗi không căn cứ trong ngày; hoặc ≥ 1 tin `notify_carrier` lộ trường cấm; hoặc một hãng còn **1 strike** nữa là bị đình chỉ (GHSH: 2/3). **Vàng** (báo NV-HANH duyệt tay mọi lỗi hãng đó trong ngày): một hãng chạm 2 lỗi tự động/ngày (`ops_limits.max_auto_strikes_per_carrier_per_day`); hoặc hãng khiếu nại ≥ 1 lỗi trong tuần đối soát. Báo qua `operations.alert_channel`. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | (1) Tracking tự ghi sai `delay_cause = CARRIER` thì lỗi oan trông vẫn "có căn cứ"; chỉ khiếu nại của hãng mới lộ ra, trễ tới một tuần. (2) Chỉ kiểm **tên trường**: số điện thoại khách viết lẫn trong trường `district` hay trong `send_reply` thì không bắt được. (3) Không đo thiệt hại cho **khách** (hoàn thiếu, báo sai số tiền), phần đó thuộc `reply_matches_ledger` của PRD v1.1 §3. (4) PRD v1.1 §6: chưa có dữ liệu người thật, nên ngưỡng vàng có thể quá nhạy hoặc quá lỏng khi lên pilot. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | | |
| `wrongful_refund_vnd_max` | | |
| `wrongful_carrier_faults_max` | | |
| `pii_leaks_max` | | |
| nên có: `escalation_rate_max` | | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): ____
- Ngưỡng chuyển cho người duyệt: ____

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
