from datetime import datetime, timedelta
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from airflow import DAG
from etl_data_weather import extract_data_weather, transform_data_weather, load_data_weather
from dataset.weather_data_api import get_weather_data
from spark.build_spark import install_spark_dependencies
from my_minio.upload import upload_to_minio

default_args = {
    'owner': 'BAI_TEST',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 9),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_etl_weather():
    df = extract_data_weather()
    df = transform_data_weather(df)
    load_data_weather(df)

with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for api weather data',
    schedule='*/30 * * * *',  #'0 10 * * *' Chạy hàng ngày 10h
    catchup=False
) as dag:
    weather_data_task = PythonOperator(
        task_id='data_weather',
        python_callable=get_weather_data
    )
    weather_data_mino_task = PythonOperator(
        task_id='data_mino',
        python_callable= upload_to_minio
    )
    install_spark_task = PythonOperator(
        task_id='install_spark',
        python_callable=install_spark_dependencies
    )

    with TaskGroup('etl_data_weather'):
        # extract_data_weather_task = PythonOperator(
        #     task_id='extract',
        #     python_callable=extract_data_weather
        # )
        # transform_data_weather_task = PythonOperator(
        #     task_id='transform',
        #     python_callable=lambda: transform_data_weather(extract_data_weather())
        # )
        load_data_weather_task = PythonOperator(
            task_id='extract_transform_load',
            python_callable=run_etl_weather
        )

    [weather_data_task, install_spark_task] >> weather_data_mino_task>> load_data_weather_task
