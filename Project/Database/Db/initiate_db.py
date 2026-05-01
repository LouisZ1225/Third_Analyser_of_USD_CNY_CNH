import sqlite3

def init_db(DB_PATH): 
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fx_daily (
        date TEXT PRIMARY KEY,
        usd_cny REAL,
        usd_cnh REAL
        )                
        """)