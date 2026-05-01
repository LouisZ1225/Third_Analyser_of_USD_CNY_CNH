import sqlite3
import pandas as pd

def query_rate(DB_PATH, table_name):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df