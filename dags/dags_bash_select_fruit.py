from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 8, 1, tz="Asia/Seoul"),
    catchup=True
) as dag:

    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruits.sh orange"
    )

    t2_peach = BashOperator(
        task_id="t2_peach",
        bash_command="/opt/airflow/plugins/shell/select_fruits.sh peach"
    )

    t1_orange >> t2_peach