import numpy as np
import pandas as pd


def beregne_statistiske_verdier(df, kolonner):
    gjennomsnitt = {}
    median = {}
    standardavvik = {}

    for kol in kolonner:
        verdier = df[kol].values
        gjennomsnitt = np.mean(verdier)
        median = np.median(verdier)
        std = np.std(verdier)

        print(f"{kol}")
        print(f" Gjennomsnitt: {gjennomsnitt:.2f}")
        print(f" Median {median:.2f}")
        print(f" Standardavvik: {std:.2f}\n")
        


