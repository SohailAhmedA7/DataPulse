import os
from urllib.parse import quote_plus
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{quote_plus(DB_PASSWORD)}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(DATABASE_URL)


def extract_orders():
    query = """
        SELECT
            o.order_id,
            o.order_date,
            o.customer_id,
            c.first_name || ' ' || c.last_name AS customer_name,
            o.product_id,
            p.product_name,
            p.category,
            o.quantity,
            p.price AS unit_price,
            o.quantity * p.price AS revenue,
            o.status
        FROM orders o
        JOIN customers c
            ON o.customer_id = c.customer_id
        JOIN products p
            ON o.product_id = p.product_id
        ORDER BY o.order_date;
    """

    df = pd.read_sql(query, engine)

    print("\nExtraction successful!")
    print(f"Rows extracted: {len(df)}")
    print("\nFirst 5 records:")
    print(df.head())
    return df


if __name__ == "__main__":
    extract_orders()