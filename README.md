<p align="center">
  <a href="https://www.uit.edu.vn/">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học CNTT" width="400">
  </a>
</p>

<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>
<h2 align="center"><b>Lab 2 - Serving model qua API và đóng gói với docker</b></h2>

---

## Thông tin sinh viên
- **Họ tên**: Mai Văn Tân
- **MSSV**: 22521301

---

## Giới thiệu

Dự án này là một ứng dụng MLOps, sử dụng Docker để đóng gói và triển khai mô hình học máy. Dự án bao gồm các thành phần chính như API, MLflow để theo dõi thí nghiệm, và các mô hình được huấn luyện trên tập dữ liệu housing. Model được chọn từ model ở [Lab 1](https://github.com/tanmaivan/cs317). Sau build bằng Docker, image cũng đã được push lên Docker Hub (https://hub.docker.com/repository/docker/tanmaivan/housing-price-api/general)

- Demo xem tại: [https://www.youtube.com/watch?v=DLQXNl660y0&ab_channel=TanMai](https://youtu.be/DLQXNl660y0)
- Video demo việc deploy được API trên server khác môi trường với máy development: [https://youtu.be/ItyNCLoofSg](https://youtu.be/ItyNCLoofSg)

## Cài đặt môi trường

1. Clone repository:

    ```bash
    git clone https://github.com/tanmaivan/mlops_lab2.git
    cd mlops_lab2
    ```

2. Tạo môi trường ảo và kích hoạt:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    # hoặc
    .\venv\Scripts\activate  # Windows
    ```

3. Cài đặt dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Cài đặt Docker và Docker Compose:
    - Đảm bảo bạn đã cài đặt Docker và Docker Compose trên máy của mình. Tham khảo [hướng dẫn cài đặt Docker](https://docs.docker.com/get-docker/) và [hướng dẫn cài đặt Docker Compose](https://docs.docker.com/compose/install/).

## Chạy ứng dụng bằng Docker

1. Build và chạy các container:

    ```bash
    docker-compose up --build
    ```

2. Sau khi các container đã chạy, bạn có thể truy cập:
    - API: http://localhost:8000

## Cấu trúc dự án

-   `src/`: Chứa mã nguồn của ứng dụng
-   `data/`: Chứa dữ liệu huấn luyện
-   `models/`: Chứa các mô hình đã được huấn luyện
-   `artifacts/`: Chứa các artifact từ quá trình huấn luyện
-   `Dockerfile`: Cấu hình để build Docker image
-   `docker-compose.yml`: Cấu hình để chạy các container

