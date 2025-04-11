import unittest #for å lage unit testene
import pandas as pd #dataframe
import numpy as np


def temperatur_kategori(temp): 
    if temp < 10:
        return "Kaldt" #definerer når det er kaldt
    elif temp < 20:
        return "Mildt" #når det er mildt
    else: 
        return "Varmt" # når det er varmt
    
def unormalt_hopp_temp(diff):
    return abs(diff)>20 #unormalt viss temperaturen hopper med over 20 grader

def kategoriserer_trykk(trykk): 
    #definerer når trykket er høytrykk eller lavtrykk
    return "Høytrykk" if trykk > 1013 else "Lavtrykk"

def kategoriserer_nedbor(nedbor):
    if nedbor == 0:
        return "Tørt" #ingen nedbør
    elif nedbor < 5:
        return "Våt luft" # yr i lufta
    elif nedbor < 20:
        return "Mye regn" # regner mye
    else:
        return "Ekstremvær"   #ekstremt vær 



