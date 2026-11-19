# Báo cáo cá nhân · Hoàng Thị Thanh Nga · 2A202604079

- **Bàn:** NgaMy · L3B · repo `K5-L3B-DAY10-NgaMy-PoCtoPilotGate1`
- **Vai:** Sản phẩm và kinh doanh
- **Phân công:** [TEAM.md · Phân công công việc](../TEAM.md#phân-công-công-việc)

## 1. Phạm vi phụ trách

| Câu | Mục phiếu / file | Việc phụ trách |
|---|---|---|
| 1.1, 1.6 | Phiếu A · A1, A4 | Mục tiêu hệ thống, tiêu chí thành công và ranh giới đầu ra |
| 1.5 | Phiếu A · A3 | Ghi cách đọc khoảng tin cậy theo thống nhất của bàn |
| Ký tiêu chí | Phiếu A · A5; `config/acceptance_criteria.json` | Điền ngưỡng, ký và push trước lần chạy đánh giá đầu |
| 2.3 | Phiếu B · B3 | Bản đồ nguồn dữ liệu và ví dụ drift chính sách |
| 2.9 | Phiếu B · B7.4; `config/operating_gates.json` mục `business` | Trần hoàn ngày, ngân sách chi phí, phạm vi pilot và ROI tối thiểu |
| Quyết định v1 | Phiếu B · B8 | Ghi quyết định Gate 1 vòng 1 |
| 3.2 | Phiếu C · C5 | Specification về payer, số tiền và approval |
| 3.5 | Phiếu C · C7 dòng kinh doanh | ROI, chi phí theo phân khúc, rủi ro đổi chính sách và hành động theo dõi |
| Quyết định v2 | Phiếu C · C12; `submission/submission.json` | Ghi quyết định v2 và ba dòng bắt buộc cùng bàn |

## 2. Việc đã hoàn tất

- Điền và ký tiêu chí chấp nhận; commit `ffb7bc8`, hash `416b7554`. Tiêu chí được ký lúc 15:12:09, trước lần đánh giá đầu tiên lúc 15:19:42.
- Cấu hình cổng kinh doanh: hoàn tự động tối đa 2.000.000đ/ngày, chi phí máy tối đa 1.500đ/ticket, phạm vi HN + HCM và `roi_min = 0,2`.
- Hoàn thành bản đồ dữ liệu/drift tại B3. REFUND-v4 có hiệu lực ngày 01/12/2026 được ghi nhận là rủi ro cần đánh giá lại.
- Ghi quyết định v1 **Tiếp tục pilot có giám sát tại HN + HCM** ở B8, commit `dc6694f`, dựa trên `R-base-prepared-20261119-154502-219163`; checkpoint vòng 1 `cccf2852`.
- Hoàn thành C5 và dòng kinh doanh C7. Đề xuất chuyển ticket không xác định được kho sang xử lý tay được ghi rõ là đề xuất vận hành, chưa được mã hóa trong `guards.py`.
- Ghi quyết định v2 **Tiếp tục trong phạm vi HN + HCM** và ba dòng bắt buộc tại C12/`submission.json`; cả bàn xác nhận.

## 3. Kết quả và bằng chứng

| Bằng chứng | Mã / vị trí | Kết quả |
|---|---|---|
| Tiêu chí đã ký | Commit `ffb7bc8`; hash `416b7554` | Ký trước lần chạy đánh giá đầu |
| Chốt vòng 1 | `config/round1.lock`; hash `cccf2852` | Đã chốt |
| Quyết định v1 | Commit `dc6694f`; `R-base-prepared-20261119-154502-219163` | Tiếp tục pilot có giám sát HN + HCM |
| Thẻ S2: base / prepared / after | `R-S2-before-20261119-171801-9b688d` / `R-S2-prepared-20261119-171801-9b688d` / `R-S2-after-20261119-171801-9b688d` | Sau sửa: pass rate 1,0; hoàn sai 0đ; lỗi hãng oan 0; lộ PII 0 |
| Grade S2 | `R-S2-grade-20261119-171800-9b688d` | `PASS-VISIBLE`; 6/6 mục kiểm tra đạt; hidden tests chưa chạy |
| Bộ nền sau sửa | `R-base-after-20261119-171745-9b688d` | Chi phí 5.550đ/ticket; ROI 0,8; không regression |
| S2 sau sửa | `submission/runs/grade-report.md` | Chi phí 8.365đ/ticket; ROI 0,2 (đúng ngưỡng); coverage 0,3333; hoàn tự động 25.000đ/ngày |

**Rủi ro còn theo dõi:** ROI S2 sát ngưỡng và `directive_obeyed_rate` vẫn 0,8 dù các cổng chặn được tác hại tiền; cần đo lại ROI/tỷ lệ chuyển người sau khi REFUND-v4 có hiệu lực và trước khi mở rộng pilot.

## 4. Dùng AI

Dùng ChatGPT để đọc hướng dẫn, rà câu chữ và kiểm tra tính nhất quán giữa tiêu chí, số liệu kinh doanh và quyết định. Các ngưỡng và quyết định được đối chiếu với config, phiếu và kết quả chạy chính thức của bàn.

## 5. Exit ticket

- **Một điều học được:** số an toàn tổng thể có thể che phân khúc có chi phí cao hơn làm tay hoặc ROI sát ngưỡng; cần xem kết quả theo kho và gắn ngưỡng với hành động cụ thể.
- **Một điều còn chưa chắc:** ROI và tỷ lệ chuyển người sau khi REFUND-v4 có hiệu lực, cũng như tỷ lệ ticket không xác định được kho trong dữ liệu thật; cần đo trong pilot trước khi mở rộng.

## 6. Việc còn lại

Phần nội dung và bằng chứng repo của Nga đã hoàn tất. Mỗi thành viên vẫn cần tự nộp liên kết repo trên LMS theo hướng dẫn của lớp.
