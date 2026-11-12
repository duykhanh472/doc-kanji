# Neko Kanji Quiz (Trắc nghiệm Đọc Kanji)

Ứng dụng web trắc nghiệm giúp luyện tập và kiểm tra cách đọc chữ Hán (Kanji) theo chuẩn các cấp độ JLPT từ N5 đến N1, hỗ trợ giao diện và nghĩa tiếng Việt đầy đủ.

## Tính năng chính (Features)

- **Các cấp độ JLPT (N5 - N1)**: Lựa chọn cấp độ phù hợp để ôn tập.
- **Dữ liệu nghĩa Tiếng Việt**: Toàn bộ từ vựng được đối chiếu và cập nhật nghĩa tiếng Việt chi tiết từ từ điển Nhật - Việt (bao gồm âm Hán - Việt và giải nghĩa các tầng nghĩa).
- **Chế độ tính giờ (Time Attack)**: Thử thách phản xạ và độ chính xác trong thời gian giới hạn (30 giây - 5 phút).
- **Gợi ý (Hints)**: Bật hiển thị ý nghĩa từ vựng để hỗ trợ trong quá trình ôn luyện.
- **Theo dõi lịch sử điểm**: Lưu trữ kết quả các lần làm bài vào `localStorage`.
- **Giao diện thân thiện, tương thích di động**: Tối ưu hiển thị trên cả máy tính và điện thoại.

## Cấu trúc thư mục (Project Structure)

Dự án được sắp xếp gọn gàng theo cấu trúc:

```
doc-kanji/
├── index.html                  # Giao diện chính ứng dụng
├── README.md                   # Tài liệu hướng dẫn
├── LICENSE.txt                 # Giấy phép mã nguồn
├── .gitignore
├── assets/
│   ├── css/
│   │   └── style.css           # Định kiểu giao diện
│   ├── js/
│   │   ├── script.js           # Xử lý logic câu hỏi, tính giờ và điểm
│   │   └── copyrights.js       # Bản quyền hiển thị
│   ├── data/
│   │   ├── N1kan.json          # Dữ liệu Kanji N1 (đã dịch nghĩa TV)
│   │   ├── N2kan.json          # Dữ liệu Kanji N2
│   │   ├── N3kan.json          # Dữ liệu Kanji N3
│   │   ├── N4kan.json          # Dữ liệu Kanji N4
│   │   ├── N5kan.json          # Dữ liệu Kanji N5
│   │   └── N6kan.json          # Dữ liệu Kanji bổ trợ
│   └── img/
│       ├── neko-logo.ico       # Favicon
│       ├── neko-pic.png        # Logo ứng dụng
│       └── screenshots/        # Ảnh chụp màn hình minh họa
│           ├── Screenshot_31.png
│           └── Screenshot_32.png
└── scripts/
    └── update_meanings.py      # Script cập nhật nghĩa tiếng Việt từ file CSV
```

## Hướng dẫn sử dụng

1. **Khởi chạy ứng dụng**:
   Có thể mở trực tiếp qua VS Code Live Server hoặc dùng Python HTTP server:
   ```bash
   python3 -m http.server 5501
   ```
   Truy cập: `http://localhost:5501`

2. **Cách chơi**:
   - Chọn cấp độ (N5 - N1) và số lượng câu hỏi mong muốn.
   - Bật hoặc tắt tính năng Gợi ý / Chế độ tính giờ.
   - Nhập cách đọc của chữ Hán bằng chữ **hiragana** hoặc **romaji** rồi nhấn **Enter**.
   - Mỗi câu có tối đa 3 lần thử.
   - Nhập `end` vào ô đáp án nếu muốn dừng bài làm sớm.

## Giấy phép (License)

Xem chi tiết tại tệp [LICENSE](LICENSE.txt).
