# Báo cáo cá nhân · Dương Thị Huyền · 2A202604077

- **Bàn:** NgaMy · L3B · repo `K5-L3B-DAY10-NgaMy-PoCtoPilotGate1`
- **Vai:** Trưởng nhóm · Kỹ sư cổng A (cổng code `lab10/guards.py`, máy chạy chính thức)
- **Phân công cả bàn:** [TEAM.md · Phân công công việc](../TEAM.md#phân-công-công-việc)

## 1. Phạm vi phụ trách

| Câu | Mục phiếu | File | Ghi chú |
|---|---|---|---|
| 2.1 | Phiếu B · B0 (dòng 1), B1 | — | Lần đánh giá đầu tiên, sau khi Nga push commit ký |
| 2.6 | Phiếu B · B7.1, B0 | `lab10/guards.py` | 2–3 cổng, mỗi cổng ứng với một lý do B6 hoặc một dòng HAZOP B4 |
| 2.7 | Phiếu B · B7.2 | — | Hai bước tránh rò rỉ dữ liệu |
| Chốt vòng 1 | Phiếu B · B8 (phần lệnh) | `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock` (do lệnh 5 tạo) | Nga viết cột v1 |
| 3.0 | Phiếu C · C0, C1 (ghi) | `incidents/Sx/` | Kéo thẻ, lệnh 6 trước khi sửa |
| 3.5 | Phiếu C · C7 (dòng code) | `lab10/guards.py` | Sửa nguyên nhân kỹ thuật của thẻ |
| Nộp bài | — | `submission/` | Lệnh 7 tới khi `ĐỦ THÀNH PHẦN`, push cuối |

Vì `runs/` không lên git, mọi lần chạy `eval`, `gate`, `checkpoint`, `grade`, `check_submission` chính thức đều chạy trên máy mình; mình gửi mã lần chạy cho cả bàn.

## 2. Đầu vào mình chờ và đầu ra mình giao

| Mình chờ | Từ ai | Để làm gì | Hạn |
|---|---|---|---|
| Commit ký tiêu chí đã push | Nga | Chạy lần đánh giá đầu tiên (2.1) | Phút 65 |
| 2–3 lý do chọn ở pre-mortem B6 | Cả bàn (Tâm ghi) | Chọn cổng cho 2.6 | Phút 85 |
| `operating_gates.json` đủ `business` (Nga), `operations` + `legal` (Tâm); 2 ticket hiểm đã chạy (Phương) | Nga, Tâm, Phương | Lệnh 5 `checkpoint` | Phút 105 |
| C8 + monitor (Phương), C12 (Nga), C9–C11 + `submission.json` (Tâm) | Cả bàn | Lệnh 7 | Phút ~198 |

| Mình giao | Cho ai | Hạn |
|---|---|---|
| Mã lần chạy base + output `gate` | Cả bàn (B0, B1, B8) | Phút ~68 |
| Bản đầu `guards.py` đã push | Phương (B7.3 chạy `--stage after`) | Phút ~95 |
| Mã lần chạy prepared + output `gate` | Nga (B8 v1) | Phút ~110 |
| Thẻ `incidents/Sx/` đã push + report lệnh 6 mốc prepared | Cả bàn | Phút ~135 |
| Report lệnh 6 sau khi sửa (mốc after) | Nga (C12), Tâm (C9) | Phút ~185 |

## 3. Kế hoạch làm việc theo mốc

- [x] **0–15:** `git config user.name "2A202604077"`, `git config user.email "2A202604077@example.com"` (README bước 2a); `python -m unittest discover -s tests` → `Ran 13 tests … OK`. _(Còn: tự kiểm tra trên GitHub rằng 3 bạn đã được mời quyền Write.)_
- [x] **15–65:** đọc `lab10/guards.py`, `lab10/helpers.py`, `lab10/agent.py`, `lab10/tools.py`, `docs/guide.md` Phụ lục C; code sẵn P0, G1, G2, G3 (mục 4); viết B7.2. **Chưa chạy trợ lý.**
- [x] **Ráp bài nhóm (15:00):** pull commit của Nga và Tâm, thêm trần lỗi hãng vào G2, sửa mục cá nhân bị ghi nhầm trong `TEAM.md`.
- [ ] **Đang chờ:** Nga chạy `python -m lab10.criteria sign`, điền `signed_by`, push `config/acceptance_criteria.json` + `.lock`. Ngưỡng đã điền nhưng chưa ký, nên mọi bước dưới đây chưa làm được.
- [ ] **65–71:** `git pull` → `python -m lab10.eval --suite base --stage base --note "baseline"` → `python -m lab10.gate --run runs/<mã>/report.json`; điền B0, B1.
- [ ] **85–100:** code cổng → `python -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."` → `python -m unittest discover -s tests`; push bản đầu ~phút 95; điền B7.1, B7.2.
- [ ] **105–115:** `python -m lab10.checkpoint` → `python -m lab10.eval --suite base --stage prepared` → `python -m lab10.gate --run runs/<mã>/report.json`; commit và push.
- [ ] **125–135:** kéo thẻ (`git fetch …cards.git main`, `git checkout FETCH_HEAD -- incidents/Sx`, `git commit -m "Nhận thẻ Sx"`), `python -m lab10.grade --incident Sx`, push; điền C0; ghi C1.
- [ ] **155–185:** sửa `guards.py` → `python -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."` → `python -m lab10.eval --suite base --stage after --note "kiểm lại bộ nền sau khi sửa"` → `python -m lab10.grade --incident Sx`; điền C7 dòng code.
- [ ] **190–200:** `python -m lab10.check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`; push.
- [ ] **Sau demo:** trả số thử về bản v2, chạy lại lệnh 6 và 7, push lần cuối; viết exit ticket trong `TEAM.md`; nộp link LMS.

## 4. Cổng phòng ngừa vòng 1 (đã code, chưa chốt)

Mình viết cổng theo các điểm yếu đọc được trong `lab10/agent.py` và `lab10/tools.py` (đọc code, **chưa chạy trợ lý** vì tiêu chí chưa ký). Mỗi cổng chỉ dựa vào nguồn sự thật, không có mã ticket hay câu chữ cụ thể. Chi tiết ở Phiếu B mục B7.1.

| # | Cổng | Hàm | Điểm yếu trong code trợ lý mà cổng chặn | Kết quả |
|---|---|---|---|---|
| P0 | Ghim chính sách theo ngày hiệu lực | `pre_guard` | Trợ lý chọn chính sách theo cờ `index_active`, không theo `effective_from/effective_to` | Unit test OK; mã lần chạy: _chờ ký_ |
| G1 | Số tiền hoàn theo nguồn sự thật | `write_gate` · `issue_refund` | `model_override` (tin số ngày khách khai), `directive_obeyed` (chỉ thị chèn trong ticket hoặc `checkout_note` → hoàn toàn bộ, đổi `payer`), `fail_open` khi 429, `write_retry` ghi hoàn lần 2, lấy phê duyệt theo khách thay vì theo đơn | Unit test OK; mã lần chạy: _chờ ký_ |
| G2 | Lỗi hãng phải có nguyên nhân trong tracking, không quá trần lỗi tự động trong ngày | `write_gate` · `file_carrier_fault` | Nguyên nhân trống thì mặc định `CARRIER`; ghi lên hãng của kiện đầu tiên (`parcels[0]`) thay vì kiện bị trễ; `delay_days` lấy từ số khách khai; không có trần số lỗi mỗi hãng mỗi ngày (`ops_limits.max_auto_strikes_per_carrier_per_day` = 2) | Unit test OK; mã lần chạy: _chờ ký_ |
| G3 | Chỉ gửi hãng các trường được phép | `write_gate` · `notify_carrier` | Payload có `customer_note` (nguyên văn lời khách) và `recipient_contact` (tên, số điện thoại) khi đơn là quà tặng | Unit test OK; mã lần chạy: _chờ ký_ |

Kiểm tra đã chạy:
- `python -m unittest discover -s tests` → `Ran 13 tests … OK`, gồm `test_team_guards_do_not_break_base` (cổng không làm hỏng ca nào đang đúng ở bộ nền). Unit test không ghi vào `runs/journal.jsonl`.
- `grep -nE "T-0|O-1|C-0" lab10/guards.py` → không có dòng nào (không xử lý riêng theo mã).

Cần cả bàn đối chiếu khi làm B6: mỗi cổng phải ứng với một lý do pre-mortem hoặc một dòng HAZOP B4 của Tâm. Nếu B6 chọn lý do khác, mình sửa cổng trước phút 105.

### Ráp với bài của nhóm (pull lúc 15:00, sau commit `7c34351`)

| Từ ai | Đã có | Ảnh hưởng tới phần của mình |
|---|---|---|
| Tâm | A1 câu 1.2 (chị Oanh, chị Hạnh); A2 câu 1.4 (telemetry lỗi hãng / rò rỉ theo hãng mỗi ngày); PRD v1.1 chung | Câu 1.2 ghi "lỗi thứ 3 của cùng một hãng trong ngày phải chuyển người" → **thêm vào G2** trần `max_auto_strikes_per_carrier_per_day`. Câu 1.4 đo trường ngoài `carrier_notice_fields` → G3 dùng đúng danh sách cho phép này, hai bên khớp |
| Nga | `acceptance_criteria.json` đã điền ngưỡng (**chưa ký**); A1, A3, A4; B3; B7.4 và mục `business` (`daily_refund_cap_vnd` 2.000.000, `cost_budget_per_ticket_vnd` 1.500, phạm vi HN + HCM, `roi_min` 0,2) | Ngưỡng an toàn = 0 (hoàn sai, lỗi hãng oan, lộ dữ liệu) khớp mục tiêu của G1, G2, G3. Trần ngày do `tools.py` tự kiểm, G1 không trùng. Ví dụ drift B3 (REFUND-v4 từ 01/12/2026) đúng loại lỗi mà P0 đỡ |
| Phương | Chưa có commit | Chưa ráp được B2, B7.3 |

Sau khi ráp: `python -m unittest discover -s tests` → `Ran 13 tests … OK` (vẫn không làm hỏng ca đang đúng).

**Sửa nhầm chỗ trong `TEAM.md`:** commit `7c34351` của Nga ghi phần đóng góp của Nga vào mục `DuongThiHuyen-2A202604077`. Mình đã chuyển nguyên văn sang mục `HoangThiThanhNga-2A202604079` và viết lại phần của mình.

Lưu ý cho Nga và Tâm: G1 không thay `daily_refund_cap_vnd` (trần đó do `tools.py` kiểm khi Nga đặt số). G3 vẫn nên có `legal.pii_fields_blocked_to_third_party` do Tâm đặt, để có hai lớp chặn.

## 5. Nhật ký lần chạy của mình

| Mã lần chạy | Bộ · mốc | Đổi MỘT thứ gì | Kết luận |
|---|---|---|---|
| | base · base | baseline | |
| | base · after | cổng vòng 1 | |
| | base · prepared | chốt vòng 1 | |
| | Sx · prepared (lệnh 6) | chưa sửa | |
| | Sx · after | | |
| | base · after | kiểm lại bộ nền | |

## 6. Bằng chứng

- Commit: _(mã commit cổng vòng 1, chốt vòng 1, sửa vòng 2, bài nộp)_
- Report: `submission/runs/grade-report.md`, report ba mốc
- Dòng trong phiếu: Phiếu B B0, B1, B7.1, B7.2; Phiếu C C0, C1, C7

## 7. Dùng AI

- Dùng Claude để đọc đề, rubric, luật và chia việc cho 4 người (bảng phân công trong `TEAM.md`).
- Dùng Claude để đọc `agent.py` / `tools.py`, tìm điểm yếu và viết bản đầu của P0, G1–G3 trong `lab10/guards.py`, cùng nội dung B7.1–B7.2. Mình tự soát lại logic và phải giải thích được từng cổng lúc demo.

## 8. Exit ticket

- Một điều học được: …
- Một điều còn chưa chắc: …
