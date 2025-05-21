# MLOps Lab 2

## Giới thiệu

Dự án này là một ứng dụng MLOps, sử dụng Docker để đóng gói và triển khai mô hình học máy. Dự án bao gồm các thành phần chính như API, MLflow để theo dõi thí nghiệm, và các mô hình được huấn luyện trên tập dữ liệu housing. Model được chọn từ model tốt nhất ở [Lab 1](https://github.com/tanmaivan/cs317). Sau build bằng Docker, image cũng đã được push lên Docker Hub (https://hub.docker.com/repository/docker/tanmaivan/housing-price-api/general)

## Yêu cầu

-   Docker và Docker Compose
-   Git
-   Python 3.8+

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

## Demo

[Chèn link demo tại đây]




## Cấu trúc dự án

-   `src/`: Chứa mã nguồn của ứng dụng
-   `data/`: Chứa dữ liệu huấn luyện
-   `models/`: Chứa các mô hình đã được huấn luyện
-   `artifacts/`: Chứa các artifact từ quá trình huấn luyện
-   `Dockerfile`: Cấu hình để build Docker image
-   `docker-compose.yml`: Cấu hình để chạy các container

## Liên hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ qua [email của bạn].
