from statsmodels.tsa.api import VAR

def run_var(df):

    df = df[["usd_cny", "usd_cnh"]].dropna()

    model = VAR(df)
    result = model.fit(1)

    print("\n===== VAR RESULT =====")
    print(result.summary())

    return result