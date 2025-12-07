import duckdb
from config import DIR_SILVER, DIR_GOLD, DB_PATH



def calculate_gold_kpis(**kwargs):
    input_silver = DIR_SILVER / "vendas_clean.parquet"
    
    # Caminhos de saída
    path_kpi_dia     = DIR_GOLD / "kpi_melhor_dia_vendas.parquet"
    path_kpi_total   = DIR_GOLD / "kpi_faturamento_total.parquet"
    path_kpi_cliente = DIR_GOLD / "kpi_melhor_cliente.parquet"

    con = duckdb.connect(str(DB_PATH))

    # Carrega tabela base
    con.execute(f"CREATE OR REPLACE TABLE tb_silver AS SELECT * FROM read_parquet('{input_silver}')")

    # 1. KPI Dia com maior venda
    con.execute(f"""
        COPY (
            SELECT
                CAST(InvoiceDate AS DATE) AS data_venda,
                SUM(TotalAmount)          AS receita_liquida
            FROM tb_silver
            GROUP BY data_venda
            ORDER BY receita_liquida DESC
            LIMIT 1
        ) TO '{path_kpi_dia}' (FORMAT PARQUET, COMPRESSION 'ZSTD');
    """)

    # 2. KPI Faturamento Total
    con.execute(f"""
        COPY (
            SELECT SUM(TotalAmount) AS faturamento_periodo
            FROM tb_silver
            WHERE InvoiceDate BETWEEN TIMESTAMP '2010-12-01' AND TIMESTAMP '2011-12-09'
        ) TO '{path_kpi_total}' (FORMAT PARQUET, COMPRESSION 'ZSTD');
    """)

    # 3. KPI Melhor Cliente
    con.execute(f"""
        COPY (
            SELECT
                CustomerID,
                SUM(TotalAmount) AS total_gasto
            FROM tb_silver
            GROUP BY CustomerID
            ORDER BY total_gasto DESC
            LIMIT 1
        ) TO '{path_kpi_cliente}' (FORMAT PARQUET, COMPRESSION 'ZSTD');
    """)

    print(f"Sucesso: KPIs gerados na pasta {DIR_GOLD}")
    con.close()