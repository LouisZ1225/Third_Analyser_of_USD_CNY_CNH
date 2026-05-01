from Config.config import CONFIG
from Database.Db.query import query_rate
from Database.Clean.query_data_clean import clean_data
from Experiment.experiment import run_experiments
from Report.summery import build_summary_table

def load_data():
    data_config = CONFIG["data"]
    df = query_rate(
        DB_PATH=data_config["DB_PATH"],
        table_name=data_config["table_name"]
    )
    df = clean_data(df, datatype=data_config["datatype"])
    return df


def main():
    print("🚀 开始运行 pipeline...")

    df_raw = load_data()
    
    results = run_experiments(
        df_raw,
        CONFIG["experiments"]
    )   
    
    summary_df = build_summary_table(results)

    print("\n📊 Summary Table:")
    print(summary_df)
    
    print("\n🎯 Pipeline 完成")

if __name__ == "__main__":
    main()