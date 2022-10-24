from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Creating "user_processing" dag, the catchup is set to false so it wont runn old DAGs
with DAG(dag_id="user_processing", start_date=datetime(2022, 10, 24),
         schedule_interval='@daily', catchup=False) as dag:

    # Postgress operator which creates a new table if this not exist
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
