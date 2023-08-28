from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2023, 8, 26, tz="Asia/Seoul"),
    catchup=True
) as dag:

    t1 = BashOperator(
        task_id="t1",
        bash_command='echo "data_interval_end: {{ data_interval_end }}"'
    )

    t2 = BashOperator(
        task_id="t2",
        env={
            'START_DATE':'{{ ds }}',
            'END_DATE':'{{ data_interval_end | ds }}'
            },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    t1 >> t2