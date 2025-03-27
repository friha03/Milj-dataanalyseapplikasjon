import unittest
import pandas as pd
import numpy as np


def temperatur_kategori(temp): 
    if temp < 10:
        return "Kaldt"
    elif temp < 20:
        return "Mildt"
    else: 
        return "Varmt"
    
def unormalt_hopp_temp(diff):
    return abs(diff)>20

def kategoriserer_trykk(trykk): 
    return "Høytrykk" if trykk> 1013 else "Lavtrykk"

def kategoriserer_nedbor(nedbor):
    if nedbor == 0:
        return "Tørt"
    elif nedbor < 5:
        return "Våt luft"
    elif nedbor < 20:
        return "Mye regn"
    else:
        return "Ekstremvær"    



