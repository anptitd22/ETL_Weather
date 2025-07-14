import os
import cx_Oracle
from dotenv import load_dotenv

#use env
path_env = "../.env"

load_dotenv(path_env)

SQL_DSN = os.getenv("SQL_DSN")
SQL_USER = os.getenv("SQL_USER")
SQL_PASS = os.getenv("SQL_PASS")

SQL_TEST_HOST = os.getenv("SQL_TEST_HOST")
SQL_TEST_PORT = int(os.getenv("SQL_TEST_PORT", 1521))
SQL_TEST_SID = os.getenv("SQL_TEST_SID")
SQL_TEST_USER = os.getenv("SQL_TEST_USER")
SQL_TEST_PASS = os.getenv("SQL_TEST_PASS")

def get_oracle_conn():
    # Sử dụng SID
    dsn = cx_Oracle.makedsn(SQL_TEST_HOST, SQL_TEST_PORT, sid=SQL_TEST_SID)
    print(dsn)
    return cx_Oracle.connect(SQL_TEST_USER, SQL_TEST_PASS, dsn, encoding="UTF-8")

#other: use connections in airflow