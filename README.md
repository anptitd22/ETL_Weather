# Giới thiệu 

Đề bài: ETL dữ liệu thời tiết 

Gọi api lấy dữ liệu dạng json trên trang https://openweathermap.org/

Đẩy dữ liệu lên minIO bằng boto3

Đọc và tải dữ liệu bằng spark vào oracle

# CÀI ĐẶT

docker-compose build --no-cache

docker-compose up -d

docker-compose up

#các thư viện cần trong python nằm trong requirements.txt

# Lưu ý

key api: tạo từ web

quy đổi thời gian bằng https://www.epochconverter.com

tài khoản airflow:

- tk: airflow
- mk: airflow

tài khoản minIO

- tk: admin
- tk: admin123456

docker oracle

- user: system
- password: 123456
- database: BAI_TEST
- SID: XE
- docker-image: oracle-db