"""Example DAG demonstrating the usage of the BashOperator."""
from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_opaerator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 8, 10, tz="Asia/Seoul"),
    catchup=False,
    # Task에 공통적으로 넘겨줄 수 있는 파라미터
    params={"example_key": "example_value"},
) as dag:
    # run_this_last = EmptyOperator(
    #     task_id="run_this_last",
    # )

    # [START howto_operator_bash]
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )
    # [END howto_operator_bash]

    bash_t1 >> bash_t2

#     for i in range(3):
#         task = BashOperator(
#             task_id="runme_" + str(i),
#             bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
#         )
#         task >> run_this

#     # [START howto_operator_bash_template]
#     also_run_this = BashOperator(
#         task_id="also_run_this",
#         bash_command='echo "ti_key={{ task_instance_key_str }}"',
#     )
#     # [END howto_operator_bash_template]
#     also_run_this >> run_this_last

# # [START howto_operator_bash_skip]
# this_will_skip = BashOperator(
#     task_id="this_will_skip",
#     bash_command='echo "hello world"; exit 99;',
#     dag=dag,
# )
# # [END howto_operator_bash_skip]
# this_will_skip >> run_this_last

# if __name__ == "__main__":
#     dag.test()