# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments
default_args = {
    'owner': 'Eric',
    'start_date': days_ago(0),
    'email': ['eric@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='process_web_log',
    default_args=default_args,
    description='Pipeline to analyze log files and perform ETL.',
    schedule_interval=timedelta(days=1),
)

# define the tasks
extract_data = BashOperator(
    task_id='extract_data',
    bash_command="""awk '{print $1}' /home/project/acesslog.txt > extracted_data.txt""",
    dag=dag,
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command='awk \'$1 != "198.46.149.143"\' extracted_data.txt > transformed_data.txt',
    dag=dag,
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cvf weblog.tar transformed_data.txt',
    dag=dag,
)

# task pipeline
extract_data >> transform_data >> load_data