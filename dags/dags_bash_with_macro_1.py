from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2023, 8, 26, tz="Asia/Seoul"),
    catchup=True
) as dag:

    t1 = BashOperator(
        task_id="t2",
        env={
            'START_DATE':'{{ data_interval_start.in_timezone("Asia/Seoul") | ds }}', # 전월 말일
            'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}' # 1일 전
            },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    t1