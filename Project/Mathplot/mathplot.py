import matplotlib.pyplot as plt
import pandas as pd

def mathplot(df):

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["spread"])
    plt.title("CNH - CNY Spread")
    plt.xlabel("Date")
    plt.ylabel("Spread")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()