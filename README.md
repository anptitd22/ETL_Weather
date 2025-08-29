# Giới thiệu 

Đề bài: ETL dữ liệu thời tiết 

Gọi api lấy dữ liệu dạng json trên trang https://openweathermap.org/

Đẩy dữ liệu lên minIO bằng boto3

Đọc và tải dữ liệu bằng spark vào oracle

<img width="1793" height="760" alt="image" src="https://github.com/user-attachments/assets/195217ee-a82e-4eaf-8bf8-41db874d9968" />

<img width="1800" height="971" alt="image" src="https://github.com/user-attachments/assets/af6a8ad9-dd3a-4d68-97f6-958b972156fd" />

<img width="691" height="385" alt="image" src="https://github.com/user-attachments/assets/562c55cc-ac05-439f-bb2e-0b8f2302b4c5" />

ID|TEMPERATURE|DESCRIPTION      |HUMIDITY|PRESSURE|DT        |
--|-----------|-----------------|--------|--------|----------|
 4|      28.24|mây thưa         |      80|    1004|1752451200|
24|      33.78|mưa nhẹ          |      56|    1003|1752386400|
 3|      32.73|mây rải rác      |      63|    1003|1752462000|
 2|      30.07|mưa vừa          |      67|     999|1752213600|
22|       35.8|mưa nhẹ          |      51|    1001|1752472800|
27|      29.04|mây đen u ám     |      79|    1001|1752537600|
 5|      26.19|mưa vừa          |      91|    1000|1752235200|
 9|      32.93|mây đen u ám     |      59|    1001|1752397200|
13|         30|mưa nhẹ          |      78|    1001|1752591600|
16|      26.36|mây đen u ám     |      87|    1006|1752364800|
26|       30.4|mưa nhẹ          |      71|    1006|1752375600|
28|      26.89|mưa nhẹ          |      86|    1003|1752300000|
31|      35.52|mây cụm          |      51|     999|1752483600|
36|      36.84|mây cụm          |      48|     999|1752559200|
 6|      26.34|mưa nhẹ          |      88|    1006|1752332400|
 7|      25.49|mưa nhẹ          |      94|    1001|1752256800|
20|       37.4|mây cụm          |      45|     998|1752570000|
33|      27.01|mưa nhẹ          |      85|    1003|1752321600|
37|      25.18|mây cụm          |      93|    1004|1752354000|
11|      28.14|mưa nhẹ          |      84|    1001|1752516000|
15|      31.11|mưa nhẹ          |      72|    1001|1752494400|
25|       30.3|mây đen u ám     |      71|    1002|1752408000|
30|       28.8|mưa nhẹ          |      76|    1002|1752310800|
35|      29.96|mưa vừa          |      75|     998|1752224400|
39|      28.97|mây cụm          |      79|    1002|1752505200|
 8|      25.95|mưa nhẹ          |      92|    1002|1752246000|
18|      32.31|mưa nhẹ          |      68|     999|1752580800|
19|      29.21|mưa nhẹ          |      82|    1000|1752602400|
34|      27.27|mưa nhẹ          |      81|     999|1752202800|
38|      25.61|mưa nhẹ          |      91|    1005|1752343200|
 1|       28.4|mây cụm          |      81|    1005|1752418800|
10|      28.87|mây đen u ám     |      83|    1000|1752613200|
23|      25.22|mưa vừa          |      95|    1001|1752267600|
12|      26.93|mây rải rác      |      86|    1003|1752440400|
14|      26.72|mưa vừa          |      89|     998|1752192000|

# CÀI ĐẶT
Tải instantclient-basic-linux.x64-23.8.0.25.04.zip

https://drive.google.com/file/d/118ADdJCFTtUn9iUbtroeVdTdDpp_rE8f/view?usp=drive_link

Đặt vào install/instantclient-basic-linux.x64-23.8.0.25.04.zip

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
