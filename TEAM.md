# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NgaMy
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-NgaMy-PoCtoPilotGate1` (https://github.com/duongthuyen/K5-L3B-DAY10-NgaMy-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): _(điền ở phút 125)_

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Dương Thị Huyền | 2A202604077 | Kỹ sư cổng A (cổng code `lab10/guards.py`, máy chạy chính thức) | ✅ |
|   2 | Hoàng Thị Thanh Nga | 2A202604079 | Sản phẩm và kinh doanh | |
|   3 | Bùi Thu Phương | 2A202604080 | Kỹ sư cổng B (trace, behavioral test, `lab10/monitors.py`) | |
|   4 | Phạm Minh Tâm | 2A202604097 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên:
`["DuongThiHuyen-2A202604077", "HoangThiThanhNga-2A202604079", "BuiThuPhuong-2A202604080", "PhamMinhTam-2A202604097"]`

## Phân công công việc

Đề có 3 vai; vai Kỹ sư cổng được phép 1–2 người nên bàn tách làm hai: **A** sở hữu code cổng và mọi lệnh chạy chính thức, **B** sở hữu trace, behavioral test và chỉ số theo dõi. Mỗi file / mỗi mục phiếu chỉ có **một người cầm bút**, để bốn người làm song song mà không đè lên nhau.

### Nguyên tắc làm song song

1. **Một máy chạy chính thức: máy của Huyền.** `runs/` bị `.gitignore`, `runs/journal.jsonl` nằm riêng trên từng máy, và team chấm đọc journal để kiểm "ký trước khi đo". Vì vậy chỉ Huyền chạy lệnh 2 (`eval`), 4 (`gate`), 5 (`checkpoint`), 6 (`grade`), 7 (`check_submission --collect`) và kéo thẻ. Mọi mã lần chạy ghi vào phiếu phải lấy từ máy này. Người khác được chạy `trace` (lệnh 3) trên máy mình sau khi tiêu chí đã ký; muốn thử `eval` thì nhờ Huyền chạy hoặc chỉ coi là nháp, không ghi mã đó vào phiếu.
2. **Mỗi file một chủ:** `lab10/guards.py` → Huyền · `lab10/monitors.py` → Phương · `config/acceptance_criteria.json` và `operating_gates.json` mục `business` → Nga · `operating_gates.json` mục `operations`, `legal` và `submission/submission.json` → Tâm. Ba phiếu A, B, C dùng chung, nhưng mỗi mục chỉ một người sửa (bảng dưới).
3. **Git:** trước khi sửa `git pull --rebase`, sửa đúng mục của mình, commit nhỏ, push ngay. Commit đặt tên `[Tên] Mục X: ...`. Không mở `config/acceptance_criteria.json` bằng trình soạn thảo tự định dạng sau khi ký. Không ai sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
4. **Mục "cả bàn"** (1.5, B6 pre-mortem, C1, C6 fault tree trước): họp chung ngắn, một người được chỉ định ghi vào file (ghi rõ trong bảng).

### Vòng 1 · Khối 1 (phút 15–65) · Phiếu A, chưa chạy trợ lý

| Người | Việc | File / mục | Chờ ai? |
|---|---|---|---|
| **Huyền** | Đọc `lab10/guards.py`, `lab10/helpers.py`, `docs/guide.md` Phụ lục C; phác 3–4 ý cổng (chưa chạy). Soát `team` trong tiêu chí = tên repo. Cấu hình danh tính Git theo README bước 2a | (nháp, chưa sửa file chấm) | Không |
| **Nga** | Câu 1.1; câu 1.6 (câu "Nếu … thì …", bốn câu soát, hai câu ranh giới đầu ra); điền toàn bộ `config/acceptance_criteria.json`; **ký** (lệnh 1) và push; A5 | Phiếu A · A1 (1.1), A4, A5; `config/acceptance_criteria.json` | Chờ nhẹ: đọc mục tiêu của Tâm (1.2) và metric của Phương (1.3) trước phút 45 để câu tiêu chí khớp. Không có cũng ký được |
| **Phương** | Câu 1.3 (offline metric cho một bước) | Phiếu A · A2 cột "Offline" | Không |
| **Tâm** | Câu 1.2 (chị Oanh, chị Hạnh); câu 1.4 (telemetry production, khung thời gian, ngưỡng báo động) | Phiếu A · A1 (1.2), A2 cột "Telemetry production" | Không |
| **Cả bàn** | Câu 1.5 (khoảng tin cậy), 3 phút, **Nga ghi** | Phiếu A · A3 | — |

**Điểm chờ bắt buộc #1:** mọi lệnh chạy trợ lý (`eval`, `trace`) **chờ Nga push commit ký** (`ĐÃ KÝ.`, phút ≤ 65). Huyền `git pull` rồi mới chạy lần đánh giá đầu tiên.

### Vòng 1 · Khối 2A (phút 65–85) · Phiếu B

| Người | Việc | File / mục | Chờ ai? |
|---|---|---|---|
| **Huyền** | Câu 2.1: lệnh 2 (`--stage base --note "baseline"`) rồi lệnh 4; ghi mã vào B0, đọc khối kinh doanh–vận hành và kho–hãng; khuyến nghị tự chặn / người duyệt / kết hợp. **Gửi mã lần chạy base vào nhóm chat ngay** | Phiếu B · B0 (dòng 1), B1 | Chờ #1 (Nga ký) |
| **Nga** | Câu 2.3: bản đồ dữ liệu + một ví dụ drift (từ `data/world.json`) | Phiếu B · B3 | Không |
| **Phương** | Câu 2.2: `trace --suite base --ticket T-002 --seed 55`, điền bảng soát lỗi | Phiếu B · B2 | Chờ #1 (Nga ký), chạy trace trên máy mình |
| **Tâm** | Câu 2.4: HAZOP vòng 1 (≥ 3 dòng tool ghi + ≥ 2 dòng ngoài kỹ thuật); checklist 9 nhóm, mỗi dòng một PIC có tên (dùng 4 tên trong bảng thành viên) | Phiếu B · B4, B5 | Không |
| **Cả bàn** | Câu 2.5 pre-mortem bốn lăng kính (phút 75–85): mỗi người viết sẵn lăng kính của mình (Huyền + Phương: kỹ thuật · Nga: kinh doanh · Tâm: con người–vận hành và pháp lý); chọn 2–3 lý do thành cổng. **Tâm ghi** | Phiếu B · B6 | Họp chung |

### Vòng 1 · Khối 2B (phút 85–105) · Phiếu B

| Người | Việc | File / mục | Chờ ai? |
|---|---|---|---|
| **Huyền** | Câu 2.6: code 2–3 cổng trong `pre_guard` / `write_gate`, mỗi cổng ứng với một lý do B6 hoặc một dòng HAZOP; chạy `eval --stage after` + `unittest`; ghi B7.1, thêm dòng B0. Câu 2.7: hai bước tránh rò rỉ dữ liệu | `lab10/guards.py`; Phiếu B · B7.1, B7.2, B0 | Cần B6 (phút 85). Cổng đọc số từ config (vd. `daily_refund_cap_vnd`) viết theo kiểu `if cap is not None` nên **không phải chờ Nga**; chỉ cần Nga push số trước khi chốt |
| **Nga** | Câu 2.9: mục `business` (`daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope`, `roi_min`), mỗi số một câu lý do từ `ops_limits`, `ops_facts`. **Push trước phút 95** | `config/operating_gates.json` · `business`; Phiếu B · B7.4 | Không |
| **Phương** | Câu 2.8: một tính chất + 2 ticket hiểm, chạy `trace --stage after --adhoc ...`, dán kết quả. Phương là người viết ticket, Huyền góp ý cổng | Phiếu B · B7.3 | Chờ Huyền push bản cổng đầu tiên (khoảng phút 95) để chạy `--stage after`; trong lúc chờ viết tính chất và ticket |
| **Tâm** | Câu 2.10: mục `operations` (`pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`) và `legal`; runbook phần 1–3 (cả thời hạn dừng: bao nhiêu phút, ai bấm); mục Giờ cao điểm | `config/operating_gates.json` · `operations`, `legal`; Phiếu B · B7.5, B7.6 | Phần runbook nhắc trần tiền / phạm vi pilot **chờ số `business` của Nga** (phút 95). Các phần khác làm ngay |

**Điểm chờ bắt buộc #2 (phút 100–105):** Huyền chỉ chạy lệnh 5 (`checkpoint`) khi **Nga và Tâm đã push `operating_gates.json`** và **Phương đã xác nhận 2 ticket hiểm không làm cổng hỏng**. Mỗi người nhắn "xong" trong nhóm chat.

### Vòng 1 · Chốt và quyết định v1 (phút 105–115) · Phiếu B mục B8

| Người | Việc | Chờ ai? |
|---|---|---|
| **Huyền** | Lệnh 5 → lệnh 2 `--stage prepared` → lệnh 4; gửi mã lần chạy prepared + output `gate`; commit và push hai bản chụp + `round1.lock` | Chờ #2 |
| **Nga** | Viết cột v1 ở B8 (quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho/hãng xấu nhất, ngày quyết định lại); cả bàn duyệt 2 phút; chạy lệnh commit cuối B8 | **Chờ Huyền**: mã lần chạy prepared + kết quả `gate` |
| **Phương, Tâm** | Soát lại B2, B4, B5, B7.3, B7.5 lần cuối (sau phút 115 không sửa Phiếu B) | Không |

### Vòng 2 · Khối 3 (phút 125–200) · Phiếu C

| Người | Việc | File / mục | Chờ ai? |
|---|---|---|---|
| **Huyền** | Kéo thẻ (3 lệnh), push; lệnh 6 khi chưa sửa gì; ghi C0. Sửa nguyên nhân kỹ thuật trong `guards.py`; chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, lệnh 6; ghi phần code của C7 | `lab10/guards.py`; Phiếu C · C0, C7 (dòng code) | Mọi người chờ Huyền push thẻ (phút ~130) |
| **Nga** | Câu 3.2 (specification); sửa `business` nếu thẻ do tiền / phạm vi; ghi dòng `business` của C7; **viết C12** (quyết định v2, đổi/giữ so với v1, ba dòng bắt buộc) | `config/operating_gates.json` · `business`; Phiếu C · C5 (3.2), C7 (dòng business), C12 | C12 **chờ Huyền** gửi report lệnh 6 cuối cùng (mốc after, phút ~185) |
| **Phương** | Câu 3.1 phần trace: dò ≥ 2 ticket hỏng hai kiểu khác nhau, bảng soát lỗi (≥ 1 lỗi chìm), tác hại ở mốc base. Câu 3.6: thêm một hàm vào `MONITORS`, điền C8 | Phiếu C · C2, C8; `lab10/monitors.py` | Chờ thẻ. Monitor làm độc lập, nhờ Huyền chạy lại lệnh 6 để thấy `monitor ✅` |
| **Tâm** | Câu 3.1 phần riêng theo thẻ (C3, bỏ nếu S4) và HAZOP thẻ (C4); câu 3.3 (giả định môi trường); sửa `operations`/`legal` nếu nguyên nhân về người; câu 3.7: C9, C10, C11 (checklist + runbook 4–5); điền `submission/submission.json` | `config/operating_gates.json` · `operations`, `legal`; Phiếu C · C3, C4, C5 (3.3), C7 (dòng ops/legal), C9–C11; `submission/submission.json` | C9 **chờ** bảng sửa C7 của cả ba người. `decision_v1/v2`, `three_lines` **chờ Nga** xong B8 và C12 |
| **Cả bàn** | C1 (cổng vòng 1 đỡ được gì, đối chiếu pre-mortem), **Huyền ghi**. C6 fault tree trước khi sửa (phút 150–155), **Phương ghi**, mỗi người góp một nhánh của tầng mình, lá trỏ ticket@seed | Phiếu C · C1, C6 | C6 chờ C2 của Phương |

**Điểm chờ bắt buộc #3 (phút 190–200):** Huyền chạy lệnh 7 chỉ khi Nga xong C12, Tâm xong `submission.json` và C9–C11, Phương xong C8. Sửa `[THIẾU]` theo từng người phụ trách mục đó.

### Demo và nộp (phút 200–240)

- Nói trong demo: Huyền (ba cột base · prepared · after, cổng code) · Nga (quyết định v2 và con số đỡ) · Tâm (người, quy trình, runbook) · Phương (chạy ticket hiểm, chỉ số theo dõi).
- Sau demo: Huyền trả mọi số thử về bản v2, chạy lại lệnh 6 và 7, push lần cuối.
- **Mỗi người** tự viết mục cá nhân dưới đây (Phần việc, Đóng góp, Bằng chứng, Exit ticket, có dùng AI cho việc gì) và tự nộp link repo trên LMS trước deadline.

### Tóm tắt ai chờ ai

| # | Ai chờ | Chờ ai | Output cần nhận | Khi nào |
|---|---|---|---|---|
| 1 | Huyền, Phương | Nga | Commit ký `config/acceptance_criteria.json` + `.lock` đã push | Phút 65 |
| 2 | Cả bàn (B0, B8) | Huyền | Mã lần chạy base | Phút ~68 |
| 3 | Huyền (cổng) | Cả bàn | 2–3 lý do được chọn ở B6 | Phút 85 |
| 4 | Tâm (runbook) | Nga | Số `business` trong `operating_gates.json` | Phút 95 |
| 5 | Phương (B7.3) | Huyền | Bản đầu của `guards.py` đã push | Phút ~95 |
| 6 | Huyền (checkpoint) | Nga, Tâm, Phương | `operating_gates.json` đủ ba mục; 2 ticket hiểm đã chạy | Phút 105 |
| 7 | Nga (B8 v1) | Huyền | Mã lần chạy prepared + output `gate` | Phút ~110 |
| 8 | Cả bàn (vòng 2) | Huyền | Thẻ `incidents/Sx/` đã push + report lệnh 6 mốc prepared | Phút ~135 |
| 9 | Cả bàn (C6) | Phương | Bảng soát lỗi C2 có ticket@seed | Phút ~150 |
| 10 | Tâm (C9) | Huyền, Nga, Tâm | Bảng sửa C7 | Phút ~180 |
| 11 | Nga (C12) | Huyền | Report lệnh 6 sau khi sửa (mốc after) | Phút ~185 |
| 12 | Tâm (`submission.json`) | Nga | Quyết định v1, v2, ba dòng bắt buộc | Phút ~195 |
| 13 | Huyền (lệnh 7) | Cả bàn | Mọi mục phiếu đã điền, `submission.json` đủ | Phút ~198 |

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DuongThiHuyen-2A202604077

### Phần việc phụ trách

Trưởng nhóm · Kỹ sư cổng A. Câu 2.1, 2.6, 2.7; ghi C1 và phần code của 3.5 (C7). Phiếu B mục B0, B1, B7.1, B7.2; Phiếu C mục C0, C1, C7 (dòng code). File: `lab10/guards.py`. Máy chạy chính thức: lệnh 2, 4, 5, 6, 7, kéo thẻ, push các mốc. Báo cáo chi tiết: [report/2A202604077_DuongThiHuyen.md](report/2A202604077_DuongThiHuyen.md).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## HoangThiThanhNga-2A202604079

### Phần việc phụ trách

Sản phẩm và kinh doanh. Câu 1.1, 1.6, 2.3, 2.9, 3.2, quyết định v1 và v2. Phiếu A mục A1 (1.1), A3 (ghi), A4, A5; Phiếu B mục B3, B7.4, B8; Phiếu C mục C5 (3.2), C7 (dòng business), C12. File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## BuiThuPhuong-2A202604080

### Phần việc phụ trách

Kỹ sư cổng B. Câu 1.3, 2.2, 2.8, 3.1 (phần trace), 3.6; ghi C6. Phiếu A mục A2 (cột Offline); Phiếu B mục B2, B7.3; Phiếu C mục C2, C6, C8. File: `lab10/monitors.py`.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## PhamMinhTam-2A202604097

### Phần việc phụ trách

Vận hành và pháp lý. Câu 1.2, 1.4, 2.4, 2.10, 3.1 (phần riêng theo thẻ, HAZOP thẻ), 3.3, 3.7; ghi B6. Phiếu A mục A1 (1.2), A2 (cột Telemetry); Phiếu B mục B4, B5, B6, B7.5, B7.6; Phiếu C mục C3, C4, C5 (3.3), C7 (dòng ops/legal), C9, C10, C11. File: `config/operating_gates.json` mục `operations`, `legal`; `submission/submission.json`.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
