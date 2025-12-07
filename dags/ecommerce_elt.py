import sys
sys.path.append("/opt/airflow")

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# 1. Aqui nós importamos com o nome NOVO (Correto)
from src.raw_to_bronze import ingest_raw_data 
from src.bronze_to_silver import process_bronze_to_silver
from src.silver_to_gold import calculate_gold_kpis

default_args = {
    "owner": "lucasmendes",
    "start_date": datetime(2020, 1, 1),
}

with DAG(
    dag_id="ecommerce_elt",
    default_args=default_args,
    schedule=None,
    catchup=False,
) as dag:

    task_extract = PythonOperator(
        task_id="ingest_raw_data",
        
        python_callable=ingest_raw_data, 
    )

    task_silver = PythonOperator(
        task_id="process_bronze_to_silver",
        python_callable=process_bronze_to_silver,
    )

    task_gold = PythonOperator(
        task_id="calculate_gold_kpis",
        python_callable=calculate_gold_kpis,
    )

    task_extract >> task_silver >> task_gold