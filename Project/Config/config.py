from Features.feature import calc_spread, calc_MA, calc_volatility
from Model.models import run_ols, run_adf, run_arima

CONFIG = {
    "data": {
        "datatype": "fx",
        "DB_PATH": "Database/Db/fx_rate.db",
        "table_name": "fx_daily"
    },

    "features": [
        {
            "name": "spread",
            "func": calc_spread,
            "params": {}
        },
        {
            "name": "ma",
            "func": calc_MA,
            "params": {"window": 20}
        },
        {
            "name": "volatility",
            "func": calc_volatility,
            "params": {"window": 20}
        }
    ],

    "models": [
        {
            "name": "OLS",
            "func": run_ols
        },
        {
            "name": "ADF",
            "func": run_adf
        },
        {
            "name": "ARIMA",
            "func": run_arima
        }
    ]
}