from pathlib import Path

# Garante que o projeto funcione tanto no Windows quanto no Docker 
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Cria caminhos para as camadas de dados, definindo a arquitetura medalhão
DIR_RAW = PROJECT_ROOT / "data" / "raw"
DIR_BRONZE = PROJECT_ROOT / "data" / "bronze"
DIR_SILVER = PROJECT_ROOT / "data" / "silver"
DIR_GOLD = PROJECT_ROOT / "data" / "gold"

# Cria caminhos para o banco de dados
DB_PATH = PROJECT_ROOT / "data" / "warehouse.duckdb"

# Lista de diretórios que precisam ser garantidos
_dirs_to_create = [DIR_RAW, DIR_BRONZE, DIR_SILVER, DIR_GOLD]

# Cria pastas automaticamente caso elas já não existam
for directory in _dirs_to_create:
    directory.mkdir(parents=True, exist_ok=True)