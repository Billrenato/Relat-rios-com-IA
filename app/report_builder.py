import pandas as pd
import matplotlib.pyplot as plt

def gerar_relatorio(df, caminho="output/relatorio.pdf"):
    df.to_csv("output/relatorio.csv", index=False)
    df.plot(kind="barh", x=df.columns[0], y=df.columns[1])
    plt.tight_layout()
    plt.savefig("output/grafico.png")
