import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def mathplot(df):

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["spread"], label = 'Spread')
    plt.title("CNH - CNY Spread")
    plt.xlabel("Date")
    plt.ylabel("Spread")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plotly_basic(df):
    fig = px.line(
        df,
        x=df.index,
        y="spread",
        title="CNH - CNY Spread"
    )
    fig.show()

def plotly_upgrade(df):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

#====== Spread =======

    fig.add_trace(go.Scatter(
            x=df.index,
            y=df["spread"],
            mode="lines",
            name="Spread",
            line=dict(width=1, color="cyan"),
            opacity=0.4),
            row=1,
            col=1
    )

#====== MA =======

    fig.add_trace(go.Scatter(
            x=df.index,
            y=df["ma_20"],
            mode="lines",
            name="MA(20)",
            line=dict(width=2, color="orange"),
            opacity=0.8),
            row=1,
            col=1
    )

#====== volatility ======

    fig.add_trace(go.Scatter(
            x=df.index,
            y=df["volatility"],
            mode="lines",
            name="Volatility",
            line=dict(width=1, color="purple")),
            row=2,
            col=1
    )

#====== 0轴 ======= 

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="gray"
    )
    
    fig.update_layout(
        title="CNH - CNY Spread Analysis | Mean Reversion Signal Monitor",
        xaxis_title="Date",
        yaxis_title="Spread",
        template="plotly_dark",
        hovermode="x unified"
    )

    fig.show()