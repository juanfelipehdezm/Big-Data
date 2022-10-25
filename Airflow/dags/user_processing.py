from cgitb import text
import http
from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
import json
import pandas as pd
from airflow.operators.python import PythonOperator

# function to transform the json we receive from the API


def process_user(ti):
    # we bring the result from the extract_user operator
    user = ti.xcom_pull(task_ids="extract_user")
    user = user["results"][0]
    processed_user = pd.json_normalize(
        {"firstname": user["name"]["first"],
         "lastname": user["name"]["last"],
         "country": user["location"]["country"],
         "username": user["login"]["username"],
         "password": user["login"]["password"],
         "email": user["email"]
         }
    )
    processed_user.to_csv("/tmp/processed_user.csv", index=None, header=False)


# Creating "user_processing" dag, the catchup is set to false so it wont runn old DAGs
with DAG(dag_id="user_processing", start_date=datetime(2022, 10, 24),
         schedule_interval='@daily', catchup=False) as dag:

    # Postgress operator which creates a new table if this not exist/// OPERATOR = ACTION
    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="""
                CREATE TABLE IF NOT EXISTS users (
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    country TEXT NOT NULL,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL

                );
            """
    )

    # HTTP operator to check if an api is available or not /// OPERATOR = SENSOR
    is_api_available = HttpSensor(
        task_id="is_api_available",
        http_conn_id="user_api",
        endpoint="api/"
    )

    # HTTP Operator to extrac the data froma an API /// Operator = ACTION
    extract_user = SimpleHttpOperator(
        task_id="extract_user",
        http_conn_id="user_api",
        endpoint="api/",
        method="GET",
        # lambda function to pass the respond to json
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    # Python operator to execute a python function
    process_user = PythonOperator(
        task_id="process_user",
        python_callable=process_user

    )
