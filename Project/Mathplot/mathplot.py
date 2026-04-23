import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

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
    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=df.index,
            y=df["spread"],
            mode="lines",
            name="Spread",
            line=dict(width=1)
    ))

    fig.add_hline(
        y=0,
        line_dash="dash",
        line_color="gray"
    )

    fig.show()