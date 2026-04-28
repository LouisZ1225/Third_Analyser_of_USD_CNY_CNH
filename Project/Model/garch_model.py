from arch import arch_model

def run_garch(df):

    df["spread"] *= 100

    returns = df["spread"].dropna()

    model = arch_model(returns, vol="Garch", p=1, q=1)
    result = model.fit()

    print("\n===== GARCH RESULT =====")
    print(result.summary())

    return result