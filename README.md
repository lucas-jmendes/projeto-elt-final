# 🛒 Pipeline ELT de E-commerce (Airflow + DuckDB)

![Status](https://img.shields.io/badge/Status-Concluído-green) ![Python](https://img.shields.io/badge/Python-3.12-blue) ![Airflow](https://img.shields.io/badge/Apache%20Airflow-Docker-red)

Este repositório contém o projeto final de Engenharia de Dados, demonstrando um pipeline **ELT (Extract, Load, Transform)** completo. O objetivo é ingerir dados brutos de vendas, processá-los e gerar indicadores de negócio (KPIs) utilizando a **Arquitetura Medalhão** (Bronze, Silver, Gold).

---

## 🏛️ Arquitetura do Projeto

O pipeline é orquestrado pelo **Apache Airflow** rodando em containers Docker. O processamento de dados é realizado utilizando **DuckDB** e **Python**, garantindo performance no tratamento de arquivos Parquet.

### Fluxo de Dados (Medallion Architecture):

1.  🟤 **Bronze (Raw):** Ingestão do dado bruto (CSV) simulando um Data Lake.
2.  ⚪ **Silver (Clean):** Limpeza de dados, tipagem correta e deduplicação. Salvo em Parquet.
3.  🟡 **Gold (Analytics):** Agregação de dados para regras de negócio e cálculo de KPIs.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Orquestração:** Apache Airflow 2.x
* **Processamento:** DuckDB & Pandas
* **Infraestrutura:** Docker & Docker Compose
* **Formato de Dados:** CSV (Input) e Parquet (Processado)

---

## 📂 Estrutura do Repositório

```bash
├── dags/
│   └── ecommerce_elt.py       # DAG principal do Airflow (Definição do fluxo)
├── src/
│   ├── raw_to_bronze.py       # Script de ingestão
│   ├── bronze_to_silver.py    # Script de limpeza e transformação
│   └── silver_to_gold.py      # Script de agregação e KPIs
├── data/                      # Diretório local de dados (Ignorado no Git)
├── logs/                      # Logs de execução do Airflow
├── docker-compose.yaml        # Configuração dos containers e volumes
├── requirements.txt           # Bibliotecas Python necessárias
└── visualizacao.py            # Script auxiliar para validação final
```

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Docker Desktop instalado e rodando.
* Git instalado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/lucas-jmendes/projeto-elt-final.git](https://github.com/lucas-jmendes/projeto-elt-final.git)
    ```

2.  **Entre na pasta:**
    ```bash
    cd NOME_DO_REPO
    ```

3.  **Inicie o ambiente:**
    ```bash
    docker-compose up -d
    ```

4.  **Acesse a Interface do Airflow:**
    * Abra o navegador em: `http://localhost:8080`
    * Ative a DAG `ecommerce_elt` e clique em **Trigger DAG**.

5.  **Valide os Resultados:**
    ```bash
    python visualizacao.py
    ```

---

## 📊 KPIs Gerados (Camada Gold)

O pipeline entrega tabelas analíticas prontas para consumo de BI, contendo:

* **Faturamento Total:** Soma consolidada das vendas processadas.
* **Melhor Dia de Vendas:** Identificação da data com maior pico de faturamento.
* **Melhores Clientes:** Ranking de clientes com maior volume de compras.

---

## 👤 Autor

**Lucas Mendes**
Desenvolvido como parte da avaliação final da disciplina de Engenharia de Dados.