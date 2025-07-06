from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.python import PythonSensor
from datetime import datetime
from plugins.psi_sensor import check_psi_threshold

with DAG(dag_id='retrain_on_drift',
         schedule_interval='@daily',
         start_date=datetime(2023, 1, 1),
         catchup=False) as dag:

    wait_for_drift = PythonSensor(
        task_id='check_psi_drift',
        python_callable=check_psi_threshold,
        poke_interval=3600,
        timeout=7200
    )

    retrain_model = BashOperator(
        task_id='retrain_model',
        bash_command='python /mlops/scripts/train_model.py'
    )

    wait_for_drift >> retrain_model