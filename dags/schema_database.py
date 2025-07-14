import cx_Oracle
import numpy as np
import pandas as pd
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType, LongType, ArrayType, \
    DoubleType
from db_connections import get_oracle_conn

def create_schema_weather():
    schema = StructType([
    	StructField("list", ArrayType(
        	StructType([
            	StructField("dt", LongType(), True),
            	StructField("main", StructType([
                	StructField("temp", DoubleType(), True),
                	StructField("pressure", LongType(), True),
                	StructField("humidity", LongType(), True),
            	]), True),
            	StructField("weather", ArrayType(
                	StructType([
                    	StructField("description", StringType(), True),
                	])
            	), True),
        	])
    	), True)
	])
    return schema

def create_table_weather(table_name="WEATHER"):
    conn = get_oracle_conn()

    cursor = conn.cursor()

    try:

        # check exist
        cursor.execute(f"""
            BEGIN
                EXECUTE IMMEDIATE 'DROP TABLE {table_name}';
            EXCEPTION
                WHEN OTHERS THEN
                    IF SQLCODE != -942 THEN
                        RAISE;
                    END IF;
            END;
        """)

        # create schema database
        cursor.execute(f"""
            CREATE TABLE {table_name} (
                id NUMBER GENERATED ALWAYS AS IDENTITY,
                temperature FLOAT,
                description VARCHAR2(255),
                humidity FLOAT,
                pressure FLOAT,
                dt VARCHAR2(255)
            )
        """)

        conn.commit()
        print(f"Table `{table_name}` created successfully.")

    except cx_Oracle.DatabaseError as e:
        print(f"Error creating table: {e}")
        raise
    finally:
        cursor.close()
        conn.close()




