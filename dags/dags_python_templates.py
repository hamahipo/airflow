from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_templates",
    schedule="30 2 * * *",
    start_date=pendulum.datetime(2023, 8, 26, tz="Asia/Seoul"),
    catchup=True
) as dag:
    
    def py_func(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
    t1 = PythonOperator(
        task_id="t1",
        python_callable=py_func,
        op_kwargs={
            'start_date':'{{ds}}',
            'end_date':'{{data_interval_end | ds}}' 
            }
    )

    @task(task_id="python_task_1")
    def py_func2(**kwargs):
        print(kwargs)
        print('ds:' + kwargs['ds'])
        print('ts:' + kwargs['ts'])
        print('data_interval_start:' + str(kwargs['data_interval_start']))
        print('data_interval_end:' + str(kwargs['data_interval_end']))
        print('task_instance:' + str(kwargs['ti']))
        

    t1 >> py_func2()