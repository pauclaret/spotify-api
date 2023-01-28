import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def sacar_populares(df):
    df = df.explode("artist")

    df_pop = df.groupby("artist")["popularity"].mean().reset_index().sort_values(by = "popularity", ascending = False).head(10)
    
    sns.barplot(data = df_pop, x = "artist", y = "popularity", color = "#1DB954")
    plt.xticks(rotation = 45)
    plt.xlabel("", fontsize = 10)
    plt.tight_layout()
    plt.savefig("images/popularidad.png")


def numericos(df):
    df_numeric = df.select_types(include = np.number).drop(["loudness", "key", "popularity", "tempo", "mode", "duration_ms", "time_signature"], axis = 1)
    valor = df_numeric.mean().tolist()
    labels = df_numeric.columns.tolist()
    valor.append(valor[0])
    labels.append(labels[0])
    N = len(labels)
    angulos = [n/float(N)*2*np.pi for n in range(N)]
    plt.polar(angulos, valor)
    plt.fill(angulos, valor, color = "grey", alpha = 0.25)
    plt.yticks(size = 0)
    plt.xticks(angulos[:-1], labels[:-1])

