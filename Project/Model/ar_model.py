from statsmodels.tsa.ar_model import AutoReg

def run_ar(df):

    df = df.dropna()

    model = AutoReg(df["spread"], lags=1).fit()

    print("\n===== AR(1) RESULT =====")
    print(model.summary())

    return model