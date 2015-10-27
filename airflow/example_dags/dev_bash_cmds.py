







from __future__ import print_function
import airflow
import datetime
from airflow.operators import BashOperator, DummyOperator

dag = airflow.DAG(
    'dev_bash_cmds',
    start_date=datetime.datetime.utcnow(),
    default_args={'owner': 'airflow', 'provide_context': True})



valid_chars='-_.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
def sanitize(text):
	return ''.join(c for c in text if c in valid_chars)

#this is where pipeline-generated bash commands come in.... 
bash_commands = ('echo "hi russ"', 'echo "hello again"')
conclusion_command = 'echo "all done"'
conclusion = BashOperator(task_id='conclude', bash_command=conclusion_command, dag=dag)

for cmd in bash_commands: 
	cmd.rstrip()
	run_this = BashOperator(
	  task_id=sanitize(cmd), bash_command=cmd, dag=dag)
	run_this.set_downstream(conclusion)








# def push(**kwargs):
#     # pushes an XCom without a specific target
#     kwargs['ti'].xcom_push(key='value from pusher 1', value=value_1)

# def push_by_returning(**kwargs):
#     # pushes an XCom without a specific target, just by returning it
#     return value_2

# def puller(**kwargs):
#     ti = kwargs['ti']

#     # get value_1
#     v1 = ti.xcom_pull(key=None, task_ids='push')
#     assert v1 == value_1

#     # get value_2
#     v2 = ti.xcom_pull(task_ids='push_by_returning')
#     assert v2 == value_2

#     # get both value_1 and value_2
#     v1, v2 = ti.xcom_pull(key=None, task_ids=['push', 'push_by_returning'])
#     assert (v1, v2) == (value_1, value_2)


# push1 = airflow.operators.PythonOperator(
#     task_id='push', dag=dag, python_callable=push)

# push2 = airflow.operators.PythonOperator(
#     task_id='push_by_returning', dag=dag, python_callable=push_by_returning)

# pull = airflow.operators.PythonOperator(
#     task_id='puller', dag=dag, python_callable=puller)

# pull.set_upstream([push1, push2])







# from builtins import range
# from airflow.operators import BashOperator, DummyOperator
# from airflow.models import DAG
# from datetime import datetime, timedelta

# seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
#                                   datetime.min.time())
# args = {
#     'owner': 'airflow',
#     'start_date': seven_days_ago,
# }

# dag = DAG(dag_id='example_bash_operator', default_args=args)

# cmd = 'ls -l'
# run_this_last = DummyOperator(task_id='run_this_last', dag=dag)

# run_this = BashOperator(
#     task_id='run_after_loop', bash_command='echo 1', dag=dag)
# run_this.set_downstream(run_this_last)

# for i in range(3):
#     i = str(i)
#     task = BashOperator(
#         task_id='runme_'+i,
#         bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
#         dag=dag)
#     task.set_downstream(run_this)

# task = BashOperator(
#     task_id='also_run_this',
#     bash_command='echo "{{ macros.uuid.uuid1() }}"',
#     dag=dag)
# task.set_downstream(run_this_last)




