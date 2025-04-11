import numpy as np
import pandas as pd


def beregne_statistiske_verdier(df, kolonner):
    gjennomsnitt = {}
    median = {}
    standardavvik = {}

    for kol in kolonner:
        gjennomsnitt = df[kol].np.mean()