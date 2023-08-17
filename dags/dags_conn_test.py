import datetime
import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 8, 10, tz="Asia/Seoul"),
    catchup=False,
    # Task에 공통적으로 넘겨줄 수 있는 파라미터
    params={"example_key": "example_value"},
) as dag:

    t1 = EmptyOperator(
        task_id="t1"
    )

    t2 = EmptyOperator(
        task_id="t2"
    )

    t3 = EmptyOperator(
        task_id="t3"
    )

    t4 = EmptyOperator(
        task_id="t4"
    )

    t5 = EmptyOperator(
        task_id="t5"
    )

    t6 = EmptyOperator(
        task_id="t6"
    )

    t7 = EmptyOperator(
        task_id="t7"
    )

    t8 = EmptyOperator(
        task_id="t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8