import pandas as pd
import cx_Oracle
import os
from pyspark.sql import functions
from pyspark.sql.functions import explode
from pyspark.sql.types import TimestampType, FloatType, StringType
from dags.db_connections import get_oracle_conn
from dags.schema_database import create_table_weather, create_schema_weather
from dags.spark.build_spark import get_spark, write_spark

table_name = "WEATHER"
MINIO_BUCKET = "weather-data"
MINIO_FILE = "opt/airflow/dataset/weather_data.json"

spark = get_spark()

def extract_data_weather():
    print("extract data from file")

    # file my_minio
    file_boto3 = f"s3a://{MINIO_BUCKET}/{MINIO_FILE}"

    for k, v in spark.sparkContext.getConf().getAll():
        print(f"{k} = {v}")

    # spark read json
    # df = spark.read.schema(create_schema_weather()).json(file_boto3)
    df = spark.read.option("multiline", "true").schema(create_schema_weather()).json(file_boto3)

    print("spark data extracted")

    df.printSchema()
    df.show(5)
    df.count()

    # select data
    df_select = df.select(explode("list").alias("data"))

    df_select = df_select.selectExpr(
        "data.dt as dt",
        "data.main.temp as temperature",
        "data.main.pressure as pressure",
        "data.main.humidity as humidity",
        "data.weather[0].description as description"
    )
    df_select.show(5)

    print("spark data selected")

    return df_select

def transform_data_weather(df):
    print("transform data")

    # drop null all
    df = df.dropna(how='all')

    # drop duplicates
    df = df.dropDuplicates()

    # cast_type
    df = df.withColumn("dt", functions.col("dt").cast(StringType()))
    df = df.withColumn("temperature", functions.col("temperature").cast(FloatType()))
    df = df.withColumn("pressure", functions.col("pressure").cast(FloatType()))
    df = df.withColumn("humidity", functions.col("humidity").cast(FloatType()))
    df = df.withColumn("description", functions.col("description").cast(StringType()))

    # add undefined
    df = df.fillna({
        "temperature": 0.0,
        "pressure": 0.0,
        "humidity": 0.0,
        "description": "undefined"
    })

    return df


def load_data_weather(df):
    print("load data")

    try:
        # create table
        create_table_weather(table_name)
        #write table
        write_spark(df, table_name)

    except Exception as e:
        print(e)
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    load_data_weather(transform_data_weather(extract_data_weather()))





















