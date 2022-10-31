from airflow import DAG
from airflow.operators.bash import BashOperator
# we import the function from the grous folder
from groups.group_download import download_tasks
from groups.group_transform import transform_tasks
from datetime import datetime

with DAG('group_dag', start_date=datetime(2022, 1, 1),
         schedule_interval='@daily', catchup=False) as dag:

    downloads = download_tasks()

    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

    transforms = transform_tasks()

    downloads >> check_files >> transforms
