# Giới thiệu 

Đề bài: ETL dữ liệu thời tiết 

Gọi api lấy dữ liệu dạng json trên trang https://openweathermap.org/

Đẩy dữ liệu lên minIO bằng boto3

Đọc và tải dữ liệu bằng spark vào oracle

<img width="1793" height="760" alt="image" src="https://github.com/user-attachments/assets/195217ee-a82e-4eaf-8bf8-41db874d9968" />

<img width="1800" height="971" alt="image" src="https://github.com/user-attachments/assets/af6a8ad9-dd3a-4d68-97f6-958b972156fd" />

<img width="691" height="385" alt="image" src="https://github.com/user-attachments/assets/562c55cc-ac05-439f-bb2e-0b8f2302b4c5" />


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
