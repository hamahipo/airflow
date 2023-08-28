from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 2 * * 1",
    start_date=pendulum.datetime(2023, 8, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:

    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=regist2,
        op_args=['yljo','female','kr','seoul'],
        op_kwargs={'email':'123@gmail.com','phone':'010'}
    )

    py_t1