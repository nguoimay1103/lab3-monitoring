# 🚀 Lab 3 - Giám sát và Ghi log cho FastAPI

Kho lưu trữ này triển khai hệ thống **giám sát** và **ghi log** cho ứng dụng **FastAPI**, bao gồm các công cụ:

- 📊 **Prometheus**
- 📈 **Grafana**
- 🚨 **Alertmanager**
- 🖥️ **Node Exporter**
- 🪵 **Fluentd**

---

## 📚 Mục lục

- [🔧 Cài đặt và Thiết lập Công cụ](#-cài-đặt-và-thiết-lập-công-cụ)
- [⚙️ Thiết lập Môi trường và Chạy Code](#️-thiết-lập-môi-trường-và-chạy-code)
- [🧪 Sử dụng](#-sử-dụng)
- [⚠️ Lưu ý](#️-lưu-ý)

---

## 🔧 Cài đặt và Thiết lập Công cụ

### ✅ Yêu cầu hệ thống

| Phần mềm         | Phiên bản yêu cầu     |
|------------------|------------------------|
| Docker           | ≥ 20.10.17             |
| Docker Compose   | ≥ 1.29.2               |
| Git              | ≥ 2.35.1               |
| Python           | = 3.12.3               |
| pip              | = 23.2.1               |

---

### 🛠️ Các bước cài đặt

1. **Clone kho lưu trữ**

```bash
git clone https://github.com/nguoimay1103/lab3-monitoring.git
cd lab3-monitoring
