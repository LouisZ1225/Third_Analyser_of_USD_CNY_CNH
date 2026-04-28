from statsmodels.tsa.arima.model import ARIMA

def run_arima(df):
    model = ARIMA(df["spread"], order=(1,0,1)).fit()
    print(model.summary())
    return model