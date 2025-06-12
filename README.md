
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>

## Môn học 
<a name="gioithieumonhoc"></a>
* *Môn học*: Phát triển và vận hành hệ thống máy học
* *Mã lớp*: CS317.P21
* *Year*: 2024-2025
## Giáo viên
<a name="giangvien"></a>
* *Đỗ Văn Tiến* - tiendv@uit.edu.vn
* *Lê Trần Trọng Khiêm* - khiemltt@uit.edu.vn

## Danh sách thành viên:
| Họ và tên      | MSSV | Lớp     |
| :----:        |    :----:   |          :----: |
| [Phạm Huỳnh Nhật Tân](https://github.com/tanphn?tab=repositories)      | 22521309       | CS317.P21  |
| [Phạm Nguyễn Anh Tuấn](https://github.com/nguoimay1103?tab=repositories)   | 22521610        | CS317.P21     |
| [Nguyễn Dương Quốc Thắng](https://github.com/solohito?tab=repositories)   | 22521332       | CS317.P21     |
| [Ngô Nguyễn Nam Trung](https://github.com/namtrunguit?tab=repositories)   | 22521559      | CS317.P21     |

# 🚀 Lab 3 - Giám sát và Ghi log cho FastAPI

Kho lưu trữ này triển khai hệ thống **giám sát** và **ghi log** cho ứng dụng **FastAPI**, bao gồm các công cụ:

- 📊 **Prometheus**
- 📈 **Grafana**
- 🚨 **Alertmanager**
- 🖥️ **Node Exporter**
- 🪵 **Fluentd**

## 📚 Mục lục

- [🔧 Cài đặt và Thiết lập Công cụ - Thiết lập Môi trường và Chạy Code](#-cài-đặt-và-thiết-lập-công-cụ)
- [⚙️ Thiết lập Môi trường và Chạy Code](#️-thiết-lập-môi-trường-và-chạy-code)
- [🧪 Sử dụng](#-sử-dụng)
- [⚠️ Lưu ý](#️-lưu-ý)

## Cài đặt và Thiết lập Công cụ - Thiết lập Môi trường và Chạy Code

### ✅ Yêu cầu hệ thống

| Phần mềm         | Phiên bản yêu cầu     |
|------------------|------------------------|
| Docker           | ≥ 20.10.17             |
| Docker Compose   | ≥ 1.29.2               |
| Git              | ≥ 2.35.1               |
| Python           | = 3.12.3               |
| pip              | = 23.2.1               |

### 🛠️ Các bước cài đặt
1. **Clone Kho Lưu trữ**
  ```bash
  git clone https://github.com/nguoimay1103/lab3-monitoring.git
  cd lab3-monitoring
  ```
3. **Cài đặt Docker và Docker Compose**
  - Trên Windows: Tải và cài đặt từ Docker Desktop.
  Kiểm tra cài đặt:
  ```bash
  docker --version
  docker-compose --version
  ```
5. **Chạy Bộ Công cụ Giám sát**
  - Sử dụng Docker Compose để khởi động tất cả các dịch vụ (Prometheus, Grafana, Alertmanager, Node-exporter, Fluentd, và API):
  ```bash
  docker-compose up -d
  ```
6. **Truy cập Công cụ**

  - Fastapi: http://localhost:8000/docs
  - Prometheus: http://localhost:9090
  - Grafana: http://localhost:3000 (Thông tin đăng nhập mặc định: admin/admin)
  - Alertmanager: http://localhost:9093
  
7. **Kiểm tra Dịch vụ**
  - Kiểm tra trạng thái container:
  ```bash
  docker ps -a
  ```

## Sử dụng
1. **Gửi Yêu cầu Dự đoán (FastAPI):**
  - truy cập http://localhost:8000/docs, Dùng Fastapi để gửi ảnh đầu vào và nhận dự đoán.
2. **Truy cập Prometheus:**
  - Mở trình duyệt và vào http://localhost:9090.
  - Chọn tab "Status" > "Targets" để kiểm tra trạng thái các target (Prometheus, Node-exporter, FastAPI). Đảm bảo tất cả đều ở trạng thái Up.
3. **Giám sát Metric (Grafana):**
  - Truy cập Grafana:
      - Mở trình duyệt và vào http://localhost:3000.
      - Đăng nhập với tài khoản mặc định: admin/admin, sau đó thay đổi mật khẩu nếu cần.
  - Cấu hình Datasource:
      - Nhấn "Configuration" (biểu tượng bánh răng) > "Data Sources" > "Add data source".
      - Chọn Prometheus.
      - Đặt URL: http://lab3-prometheus:9090.
      - Nhấn "Save & Test" để xác nhận kết nối thành công.
  - Tạo Dashboard:
      - Nhấn "Dashboard" > "New" > "Import"
      - sau đó Upload file dashboard "grafana-dashboard.json" nhấn Load
 ## Lưu ý
  ## Cấu hình Alertmanager để Gửi Thông báo qua Email
  1. **Chuẩn bị Thông tin Email**
   - Sử dụng tài khoản email có hỗ trợ SMTP (ví dụ: Gmail, Outlook).
   - Đối với Gmail, bạn cần tạo **App Password** nếu đã bật 2FA:
     - Vào [Google Account > Security > App Passwords](https://myaccount.google.com/apppasswords).
     - Tạo mật khẩu ứng dụng và lưu lại (16 ký tự).
   - Thông tin cần thiết:
     - **SMTP Host**: smtp.gmail.com (cho Gmail).
     - **SMTP Port**: 587 (cho TLS).
     - **Username**: Địa chỉ email (ví dụ: your.email@gmail.com).
     - **Password**: Mật khẩu ứng dụng hoặc mật khẩu email.
  2. **Cấu hình File alertmanager.yml**
```bash
    global:
    resolve_timeout: 5m
  
    route:
      receiver: 'email-notifications'
      group_by: ['alertname']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 12h
    
    receivers:
    - name: 'email-notifications'
      email_configs:
      - to: 'your.email@gmail.com'  # Thay bằng email của bạn
        from: 'your.email@gmail.com'  # Thay bằng email của bạn
        smarthost: 'smtp.gmail.com:587'  # Cấu hình SMTP nếu cần
        auth_username: 'your.email@gmail.com'  # Thay bằng username email
        auth_password: 'your_app_password'  # Thay bằng mật khẩu ứng dụng
        require_tls: true
```
- Link Video: https://youtu.be/PniirnRW7B8
