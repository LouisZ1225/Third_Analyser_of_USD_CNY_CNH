import sqlite3

def store_data(DB_PATH, df):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        records = df.values.tolist()

        cursor.executemany("""
        INSERT OR REPLACE INTO fx_daily(date, usd_cny, usd_cnh)
        VALUES (?, ?, ?)
        """, records)