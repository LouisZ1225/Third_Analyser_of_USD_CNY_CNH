from Clean.clean_csv import load_cnh_csv, load_cny_csv, merge_fx_data
from Database.initiate_db import init_db
from Store.store import store_data

DB_PATH = "/Users/zgzzgz/My files/Python Repositories/Third_Analyser_of _USD_CNY_CNH/Project/Database/fx_rate.db"

def run_pipeline():
    init_db(DB_PATH)
    
    df_cnh = load_cnh_csv("Database/usd_cnh.csv")
    df_cny = load_cny_csv("Database/usd_cny.csv")
    
    df = merge_fx_data(df_cny, df_cnh)
    
    store_data(DB_PATH, df)
    
    print("数据写入完成")
    
if __name__ == "__main__":
    run_pipeline()