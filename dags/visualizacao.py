import duckdb
import pandas as pd
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("\n=== VALIDAÇÃO DA CAMADA GOLD (DuckDB) ===\n")
con = duckdb.connect()

arquivo_faturamento = 'data/gold/kpi_faturamento_total.parquet'

if os.path.exists(arquivo_faturamento):
    print(f"📊 Lendo: {arquivo_faturamento}")
    df_fat = con.execute(f"SELECT * FROM '{arquivo_faturamento}'").df()
    print(df_fat)
    print("-" * 40)
else:
    print(f"⚠️ Arquivo não encontrado: {arquivo_faturamento}")

print("\n")


arquivo_clientes = 'data/gold/kpi_melhor_cliente.parquet'

if os.path.exists(arquivo_clientes):
    print(f"🏆 Lendo: {arquivo_clientes}")
    try:
        df_cli = con.execute(f"SELECT * FROM '{arquivo_clientes}' ORDER BY total_gasto DESC LIMIT 5").df()
        print(df_cli)
    except:
        print(con.execute(f"SELECT * FROM '{arquivo_clientes}' LIMIT 5").df())
        
    print("-" * 40)
else:
    print(f"⚠️ Arquivo não encontrado: {arquivo_clientes}")

print("\n=== FIM DA VALIDAÇÃO ===")