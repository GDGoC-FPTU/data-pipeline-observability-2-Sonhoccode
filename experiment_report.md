# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-XXXX
**Name:** Hoàng Ích Cao Sơn
**Date:** 2026-06-10

---

## 1. Ket qua thi nghiem

Chay `agent_simulation.py` voi 2 bo du lieu va ghi lai ket qua:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200. | 9 | Du lieu sach, category da duoc chuan hoa, khong co gia tri am/0. |
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999. | 2 | Du lieu nhiem: outlier rat lon, duplicate ID, wrong type, null values. |

---

## 2. Phan tich & nhan xet

### Tai sao Agent tra loi sai khi dung Garbage Data?


Agent trả lời sai khi dùng Garbage Data vì dữ liệu đầu vào đã bị "poisoned" và không còn đại diện cho tri thức mong muốn. Duplicate ID làm cho nguồn dữ liệu có thể bị đếm trong phân tích, wrong data types có thể gây lỗi ép kiểu hoặc làm bài toán xử lý dữ liệu bị sai, còn outliers như "Nuclear Reactor" với giá 999999 làm mô hình hoặc logic tìm "best choice" bị lệch mạnh về giá trị cực đoan. Null values và bản ghi thiếu category làm giảm độ tin cậy của tập dữ liệu, khiến agent không còn có nền tảng ổn định để rút ra câu trả lời hợp lý. Nói cách khác, agent không chỉ phụ thuộc vào prompt mà còn phụ thuộc rất nhiều vào chất lượng dữ liệu được nạp vào. Nếu đầu vào ban đầu sai, kết quả đầu ra sẽ sai theo, dù cho prompt có tốt đến đâu. Bài thí nghiệm này cho thấy data validation và data cleaning là bước bắt buộc nếu muốn agent hoạt động ổn định trong thực tế.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Đồng ý. Prompt tốt chỉ giúp mô hình hỏi đúng hơn, nhưng nếu dữ liệu đầu vào bản chất là sai, outlier, thiếu giá trị, hoặc có kiểu dữ liệu không hợp lệ thì agent vẫn có thể trả lời sai. Vì vậy, data quality là điều kiện nền tảng; prompt quality chỉ là lớp tăng tối ưu bên trên.

Kết quả thí nghiệm này cho thấy pipeline ETL cần lọc dữ liệu xấu trước khi đưa vào phần agenting. Khi dữ liệu sạch, câu trả lời đúng và có ý nghĩa hơn. Khi dữ liệu nhiễm, giá trị lỗi có thể kéo agent về một kết luận sai hoàn toàn.