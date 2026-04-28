from statsmodels.tsa.stattools import adfuller

def run_adf(df):

    result = adfuller(df["spread"].dropna())

    print("\n===== ADF TEST =====")
    print(f"ADF Statistic: {result[0]}")
    print(f"p-value: {result[1]}")