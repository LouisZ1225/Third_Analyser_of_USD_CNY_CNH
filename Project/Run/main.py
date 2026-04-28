from Calculate.calculate_MA import calc_MA
from Calculate.calculate_spread import calc_spread
from Calculate.calculate_volatility import calc_volatility
from Mathplot.mathplot import mathplot, plotly_basic,plotly_upgrade
from Database.query import query_rate
from Model.ols_model import run_ols
from Model.adf_model import run_adf
from Model.ar_model import run_ar
from Model.garch_model import run_garch
from Model.var_model import run_var
from Model.arima_model import run_arima
from Model.johansen_model import run_coint

DB_PATH = "Database/fx_rate.db"

def main():
    print("🚀 开始运行 pipeline...")

    df = query_rate(DB_PATH)
    print("✅ 数据读取完成")

    df = calc_spread(df)
    df = calc_MA(df, 20)
    df = calc_volatility(df, 20)
    
    models = [
    ("OLS", run_ols),
    ("ADF", run_adf),
    ("AR", run_ar),
    ("GARCH", run_garch),
    ("VAR", run_var),
    ("ARIMA", run_arima),
    ("JOHANSEN", run_coint)
]
    results = {}
    
    for name, func in models:
        try:
            print(f"\n📊 Running {name} model...")
            result = func(df)
            results[name] = result
            print(f"✅ {name} 完成")
        except Exception as e:
            print(f"❌ {name} 报错：{e}")
    
    print("✅ 指标计算完成")

    #plotly_upgrade(df)
    print("🎯 Pipeline 完成")

if __name__ == "__main__":
    main()