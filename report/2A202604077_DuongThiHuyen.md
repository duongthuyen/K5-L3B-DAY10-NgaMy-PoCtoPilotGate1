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

- [ ] **0–15:** `git config user.name "2A202604077"`, `git config user.email "2A202604077@example.com"` (README bước 2a); `python -m unittest discover -s tests` → `Ran 13 tests … OK`; mời collaborator quyền Write.
- [ ] **15–65:** đọc `lab10/guards.py`, `lab10/helpers.py`, `docs/guide.md` Phụ lục C; phác ý cổng. **Không chạy trợ lý.**
- [ ] **65–71:** `git pull` → `python -m lab10.eval --suite base --stage base --note "baseline"` → `python -m lab10.gate --run runs/<mã>/report.json`; điền B0, B1.
- [ ] **85–100:** code cổng → `python -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."` → `python -m unittest discover -s tests`; push bản đầu ~phút 95; điền B7.1, B7.2.
- [ ] **105–115:** `python -m lab10.checkpoint` → `python -m lab10.eval --suite base --stage prepared` → `python -m lab10.gate --run runs/<mã>/report.json`; commit và push.
- [ ] **125–135:** kéo thẻ (`git fetch …cards.git main`, `git checkout FETCH_HEAD -- incidents/Sx`, `git commit -m "Nhận thẻ Sx"`), `python -m lab10.grade --incident Sx`, push; điền C0; ghi C1.
- [ ] **155–185:** sửa `guards.py` → `python -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."` → `python -m lab10.eval --suite base --stage after --note "kiểm lại bộ nền sau khi sửa"` → `python -m lab10.grade --incident Sx`; điền C7 dòng code.
- [ ] **190–200:** `python -m lab10.check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`; push.
- [ ] **Sau demo:** trả số thử về bản v2, chạy lại lệnh 6 và 7, push lần cuối; viết exit ticket trong `TEAM.md`; nộp link LMS.

## 4. Cổng phòng ngừa (điền sau khi code)

| # | Cổng | Hàm (`pre_guard` / `write_gate`) | Ứng với (lý do B6 / dòng HAZOP) | Kết quả (mã lần chạy) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

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
- _(ghi thêm nếu dùng AI khi viết cổng hay soát phiếu)_

## 8. Exit ticket

- Một điều học được: …
- Một điều còn chưa chắc: …
