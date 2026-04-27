import pandas as pd
import statsmodels.api as sm

def run_ols(df):

    df = df.copy()
    df = df.dropna()
    
    df["spread_lag1"] = df["spread"].shift(1)

    df = df.dropna()

    X = df[["spread_lag1", "volatility"]]
    X = sm.add_constant(X)
    
    y = df["spread"]

    model = sm.OLS(y, X).fit()

    print("\n===== OLS RESULT =====")
    print(model.summary())

    return model