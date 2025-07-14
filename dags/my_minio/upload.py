import os
import boto3
from botocore.client import Config

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../dataset/weather_data.json"))

def upload_to_minio(bucket_name="weather-data", object_name=None):
    # name file
    if object_name is None:
        object_name = file_path

    # boto3
    s3 = boto3.client(
        's3',
        endpoint_url="http://minio:9000",
        aws_access_key_id="admin",
        aws_secret_access_key="admin12345",
        config=Config(signature_version='s3v4'),
        region_name='us-east-1'
    )

    # create bucket
    try:
        s3.head_bucket(Bucket=bucket_name)
    except:
        s3.create_bucket(Bucket=bucket_name)

    # upload file
    s3.upload_file(file_path, bucket_name, object_name)
    print(f"Upload thành công: {object_name} lên bucket {bucket_name}")

if __name__ == "__main__":
    upload_to_minio()