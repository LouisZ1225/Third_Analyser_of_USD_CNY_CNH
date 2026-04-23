from Calculate.calculate_MA import calc_MA
from Calculate.calculate_spread import calc_spread
from Calculate.calculate_volatility import calc_volatility
from Mathplot.mathplot import mathplot, plotly_basic,plotly_upgrade
from Database.query import query_rate

DB_PATH = "Database/fx_rate.db"

def main():
    print("🚀 开始运行 pipeline...")

    # 1️⃣ 读取数据
    df = query_rate(DB_PATH)
    print("✅ 数据读取完成")

    # 2️⃣ 计算指标
    df = calc_spread(df)
    df = calc_MA(df, 20)
    df = calc_volatility(df, 20)

    print("✅ 指标计算完成")

    # 3️⃣ 画图
    plotly_upgrade(df)

    print("🎯 Pipeline 完成")

if __name__ == "__main__":
    main()