import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from Service.service_ui import service_ui

import streamlit as st
import pytz
from datetime import date, datetime
china_tz = pytz.timezone("Asia/Shanghai")
china_today = datetime.now(china_tz).date()

# ===== 界面模块 ======

st.title("💱 Louis的汇率查询助手")
            

# ===== 用户输入模块 ======

date = st.date_input("选择日期", value = china_today)
data = str(date)
base = st.selectbox("基准货币", 
                    list(CURRENCIES.keys()),
                    format_func=lambda x: f"{FLAGS.get(x, '🌍')} {x} - {CURRENCIES[x]} "
)
target = st.selectbox("目标货币", 
                    list(CURRENCIES.keys()),
                    index = list(CURRENCIES.keys()).index("CNY"),
                    format_func=lambda x: f"{FLAGS.get(x, '🌍')} {x} - {CURRENCIES[x]}"
)

# ===== 结果展示模块 ======

if st.button("查询"):
    
    result = service_ui(data, base, target)

    if result["status"] == "success":
        st.success(result["message"])

    elif result["status"] == "no_data":
        st.warning(result["message"])