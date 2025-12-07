import shutil
from datetime import datetime
from config import DIR_RAW, DIR_BRONZE

def ingest_raw_data(**kwargs):
    """
    Copia os dados da camada RAW para BRONZE.
    """
    
    # 1. Definição de origem e destino
    input_path = DIR_RAW / "ecommerce_data.csv"
    
    # Gera data no formato YYYYMMDD para o nome do arquivo
    today_str = datetime.now().strftime("%Y%m%d")
    
    # Nome do arquivo de saída com base na data
    output_filename = f"vendas_raw_{today_str}.csv"
    output_path = DIR_BRONZE / output_filename

    # 2. Executa a cópia
    shutil.copy(input_path, output_path)

    print(f"Sucesso: Dados ingeridos em {output_path}")
    
    # Retorna o caminho para o Airflow
    return str(output_path)