import sqlite3

def store_data(DB_PATH, df):
    with sqlite3.connect(DB_PATH) as conn:
        df.to_sql("fx_daily", conn, if_exists="replace", index=False)