[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=24112721&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** magonsilver05@gmail.com  
**Name:** Hoàng Ích Cao Sơn

---

## Mo ta

Bài lab này xây dựng một pipeline ETL đơn giản bằng Python: đọc dữ liệu JSON, kiểm tra chất lượng dữ liệu, chuẩn hóa trường category, tính giá sau giảm 10%, và lưu kết quả ra CSV. Ngoài phần ETL, repository còn có mô phỏng một agent đơn giản để minh họa tác động của dữ liệu sạch vs dữ liệu “garbage” lên kết quả trả lời.

---

## Cach chay (How to Run)

### Prerequisites
```bash
pip install pandas
```

### Chay ETL Pipeline
```bash
python solution.py
```

### Chay Agent Simulation (Stress Test)
```bash
python agent_simulation.py
```

---

## Cau truc thu muc

```
├── solution.py              # ETL Pipeline script
├── processed_data.csv       # Output cua pipeline
├── experiment_report.md     # Bao cao thi nghiem
└── README.md                # File nay
```

---

## Kết quả

Chạy với `raw_data.json` cho ra 3 record hợp lệ và loại 2 record lỗi. File output `processed_data.csv` có các cột `discounted_price` và `processed_at`, trong đó `category` đã được chuẩn hóa sang Title Case. Khi chạy `agent_simulation.py`, bộ dữ liệu sạch trả về câu trả lời hợp lý, còn bộ dữ liệu garbage vẫn có thể làm agent đưa ra câu trả lời sai nếu không có thêm layer validation.

### Ghi chú
- 'solution.py' đã được cài đặt để không crash nếu thiếu file input.
- 'generate_garbage.py' tạo ra dữ liệu xấu để test độ bền của pipeline và agent.
- 'experiment_report.md' ghi lại kết quả thí nghiệm và phân
