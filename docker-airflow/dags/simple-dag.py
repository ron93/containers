import datetime as dt 
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python import PythonOperator

def greet():
    print('Writing in file')

    with open('./file/greet.txt' , 'a+' ,encoding='utf8') as f:
        now = dt.datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M")
        f.write(str(t) + '\n')
    return 'Greeted'

def respond():
    return 'Greet Responded Again'


default_args = {

    'owner' : 'airflow',
    #date to start executing workflow
    'start_date' : dt.datetime(2020, 2, 13, 12, 00),
    #no. of processes -- used when running multiple dags
    'concurrency' : 1 ,
    #no of retries incase of execution fail
    'retries' :0
}

#context manager  -- manages resources 
#simple-dag -- dag id
with DAG('simple-dag', 
        default_args=default_args,
        schedule_interval='*/10 * * * *',
        ) as dag:

        #operator with assigned task ids
        opr_hello = BashOperator(task_id = 'say_Hi',
                                bash_command='echo "Hi!!"')

    #python callable -- calls python functions above 

        opr_greet = PythonOperator(task_id='greet',
                                python_callable=greet)
        
        opr_sleep = BashOperator(task_id='sleep_me',
                                bash_command='sleep 5')
        
        opr_respond = PythonOperator(task_id='respond',
                                    python_callable=respond)


opr_hello >> opr_greet >> opr_sleep >> opr_respond