from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 2 * * *",
    start_date=pendulum.datetime(2023, 8, 26, tz="Asia/Seoul"),
    catchup=True
) as dag:

    @task(task_id="python_task_1")
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)
    
    python_task_1 = show_templates()