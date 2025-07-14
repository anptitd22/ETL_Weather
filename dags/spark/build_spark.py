from dotenv import load_dotenv
from pyspark import SparkConf
from pyspark.sql import SparkSession
import os

path_env = "../.env"

load_dotenv(path_env)

SQL_DSN = os.getenv("SQL_DSN")
SQL_USER = os.getenv("SQL_USER")
SQL_PASS = os.getenv("SQL_PASS")

SQL_TEST_USER = os.getenv("SQL_TEST_USER")
SQL_TEST_PASS = os.getenv("SQL_TEST_PASS")
SQL_TEST_SID = os.getenv("SQL_TEST_SID")
SQL_TEST_HOST = os.getenv("SQL_TEST_HOST")
SQL_TEST_PORT = os.getenv("SQL_TEST_PORT")
SQL_TEST_ORACLE_DOCER = os.getenv("SQL_TEST_ORACLE_DOCER")

def get_spark():
    # setup
    return SparkSession.builder \
        .appName("BAITEST") \
        .master("local[*]") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000/") \
        .config("spark.hadoop.fs.s3a.access.key", "admin") \
        .config("spark.hadoop.fs.s3a.secret.key", "admin12345") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
        .config("spark.jars",
                "/opt/spark/jars/hadoop-aws-3.3.6.jar,/opt/spark/jars/aws-java-sdk-bundle-1.12.787.jar,/opt/spark/jars/ojdbc11.jar") \
        .config("spark.hadoop.fs.s3a.connection.timeout", "60000") \
        .config("spark.hadoop.fs.s3a.connection.establish.timeout", "5000") \
        .config("spark.hadoop.fs.s3a.connection.request.timeout", "60000") \
        .config("spark.hadoop.fs.s3a.connection.part.upload.timeout", "60000") \
        .config("spark.hadoop.fs.s3a.connection.idle.time", "60000") \
        .config("spark.hadoop.fs.s3a.threads.keepalivetime", "60000") \
        .config("spark.driver.extraClassPath", "/opt/spark/jars/ojdbc11.jar") \
        .config("spark.executor.extraClassPath", "/opt/spark/jars/ojdbc11.jar") \
        .config("spark.hadoop.fs.s3a.vectored.read.min.seek.size", "131072") \
        .config("spark.hadoop.fs.s3a.vectored.read.max.merged.size", "2097152") \
        .config("spark.hadoop.fs.s3a.impl.disable.cache", "true") \
        .config("spark.hadoop.fs.s3a.fast.upload", "true") \
        .config("spark.hadoop.fs.s3a.multipart.size", "104857600") \
        .config("spark.hadoop.fs.s3a.threads.max", "10") \
        .config("spark.hadoop.fs.s3a.connection.maximum", "15") \
        .config("spark.hadoop.fs.s3a.attempts.maximum", "3") \
        .config("spark.hadoop.fs.s3a.retry.limit", "5") \
        .config("spark.hadoop.fs.s3a.retry.interval", "500") \
        .config("spark.hadoop.fs.s3a.socket.recv.buffer", "65536") \
        .config("spark.hadoop.fs.s3a.socket.send.buffer", "65536") \
        .config("spark.hadoop.fs.s3a.multipart.purge.age", "86400") \
        .config("spark.sql.adaptive.enabled", "false") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "false") \
        .getOrCreate()

# def get_spark():
#     return SparkSession.builder \
#         .appName("BAITEST") \
#         .master("local[*]") \
#         .config("spark.hadoop.fs.s3a.endpoint", "http://127.0.0.1:9000/") \
#         .config("spark.hadoop.fs.s3a.access.key", "admin") \
#         .config("spark.hadoop.fs.s3a.secret.key", "admin12345") \
#         .config("spark.hadoop.fs.s3a.path.style.access", "true") \
#         .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
#         .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
#         .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false") \
#         .config("spark.jars",
#                     "/opt/spark/jars/hadoop-aws-3.3.6.jar,/opt/spark/jars/aws-java-sdk-bundle-1.12.787.jar,/opt/spark/jars/ojdbc11.jar") \
#         .config("spark.driver.extraClassPath", "/opt/spark/jars/ojdbc11.jar") \
#         .config("spark.executor.extraClassPath", "/opt/spark/jars/ojdbc11.jar") \
#         .getOrCreate()

def write_spark(df, table_name):
    # write
    return df.write \
        .format("jdbc") \
        .option("url", f"jdbc:oracle:thin:@{SQL_TEST_ORACLE_DOCER}:{SQL_TEST_PORT}/{SQL_TEST_SID}") \
        .option("dbtable", table_name) \
        .option("user", SQL_TEST_USER) \
        .option("password", SQL_TEST_PASS) \
        .option("driver", "oracle.jdbc.driver.OracleDriver") \
        .mode("append") \
        .save()

def install_spark_dependencies():
    spark = get_spark()
    print("Spark session started.")
    confs = spark.sparkContext.getConf().getAll()
    for k, v in confs:
        print(f"{k} = {v}")
    print("Spark session finished.")
    spark.stop()

