import pandas as pd
from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

ENCODED_PASSWORD = quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{ENCODED_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
engine = create_engine(DATABASE_URL)


def load_data(df):
    print("\nStarting data load...")

    df.to_sql(
        "sales_data",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully!")
    print(f"Rows loaded: {len(df)}")


if __name__ == "__main__":
    print("Testing database connection...")

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM sales_data")
        )
        count = result.scalar()

    print(f"Rows in database: {count}")