import pandas as pd
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "" # Add your password here
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "customer_data_analysis"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_data():
    query = """
    SELECT
        c.customer_id,
        c.age,
        c.annual_income,
        c.credit_limit,
        c.current_balance,
        c.num_products,
        o.responded
    FROM customers c
    JOIN offers o ON c.customer_id = o.customer_id;
    """
    return pd.read_sql(query, engine)