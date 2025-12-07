import duckdb
from config import DIR_BRONZE, DIR_SILVER, DB_PATH

def process_bronze_to_silver(**kwargs):
    """
    Lê o CSV da camada Bronze e salva em Parquet.
    """
    
    # 1. Identifica o arquivo mais recente
    files = sorted(list(DIR_BRONZE.glob("vendas_raw_*.csv")))
    
    if not files:
        raise FileNotFoundError("Nenhum arquivo encontrado na pasta Bronze!")
        
    latest_file = files[-1]
    target_path = DIR_SILVER / "vendas_clean.parquet"

    # 2. Conecta ao DuckDB
    con = duckdb.connect(str(DB_PATH))

    # 3. Carrega para Staging
    con.execute(f"""
        CREATE OR REPLACE TABLE stg_vendas AS
        SELECT * FROM read_csv_auto('{latest_file}', IGNORE_ERRORS=TRUE);
    """)

    # 4. Transformação e Limpeza
    query_transform = """
        CREATE OR REPLACE TABLE tb_silver_vendas AS
        SELECT
            InvoiceNo,
            StockCode,
            Description,
            CAST(Quantity AS INTEGER)           AS Quantity,
            CAST(UnitPrice AS DOUBLE)           AS UnitPrice,
            CustomerID,
            Country,
            
            strptime(InvoiceDate, '%m/%d/%Y %H:%M') AS InvoiceDate,
            
            -- O total pode ser negativo em caso de devolução
            (CAST(Quantity AS INTEGER) * CAST(UnitPrice AS DOUBLE)) AS TotalAmount
            
        FROM stg_vendas
        WHERE 
            CustomerID IS NOT NULL 
            AND InvoiceDate IS NOT NULL
            -- Mantemos Quantity mesmo que seja 0 ou negativo
    """
    con.execute(query_transform)

    # 5. Exporta para Parquet
    con.execute(f"""
        COPY tb_silver_vendas TO '{target_path}'
        (FORMAT PARQUET, COMPRESSION 'ZSTD');
    """)

    print(f"Sucesso: Arquivo Silver gerado em {target_path} (Incluindo devoluções)")
    
    con.close()
    return str(target_path)