from airflow import DAG
import pendulum
from airflow.decorators import task
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 2 * * 1",
    start_date=pendulum.datetime(2023, 8, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)
    
    python_task_1 = regist('yljo','female','kr','seoul')