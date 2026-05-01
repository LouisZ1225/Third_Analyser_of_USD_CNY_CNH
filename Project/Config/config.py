CONFIG = {
    "data": {
        "datatype": "fx",
        "DB_PATH": "Database/Db/fx_rate.db",
        "table_name": "fx_daily"
    },

    "features": [
        {"name": "spread"},
        {"name": "ma", "params": {"window": 20}},
        {"name": "volatility", "params": {"window": 20}},
        {"name": "lag", "params": {"lag": 1}},
        {"name": "diff", "params": {"lag": 1}}
    ],
    "experiments": [

        # 🧪 1. 基础平稳性检验
        {
            "name": "基础平稳性检验",
            "features": [
                {"name": "spread"}
            ],
            "models": ["ADF"]
        },

        # 🧪 2. 趋势解释
        {
            "name": "趋势解释",
            "features": [
                {"name": "spread"},
                {"name": "ma", "params": {"window": 20}}
            ],
            "models": ["OLS"]
        },

        # 🧪 3. 波动解释
        {
            "name": "波动解释",
            "features": [
                {"name": "spread"},
                {"name": "volatility", "params": {"window": 20}}
            ],
            "models": ["OLS", "GARCH"]
        },

        # 🧪 4. 滞后结构
        {
            "name": "滞后结构",
            "features": [
                {"name": "spread"},
                {"name": "lag", "params": {"lag": 1}}
            ],
            "models": ["OLS", "AR"]
        },

        # 🧪 5. 差分结构（用于时间序列）
        {
            "name": "差分结构",
            "features": [
                {"name": "spread"},
                {"name": "diff", "params": {"lag": 1}}
            ],
            "models": ["ARIMA"]
        },

        # 🧪 6. 协整关系
        {
            "name": "协整关系",
            "features": [
                {"name": "spread"}   # 实际用 usd_cny/usd_cnh
            ],
            "models": ["JOHANSEN"]
        }
    ]
}