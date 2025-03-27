import numpy as np
import pandas as pd
import unittest
from verdi_data import(
    temperatur_kategori,
    unormalt_hopp_temp,
    kategoriserer_trykk,
    kategoriserer_nedbor
)

class Test_Data(unittest.TestCase): 
    def test_Kategori(self): 
        self.assertEqual(temperatur_kategori(-2), "Kaldt")
        self.assertEqual(temperatur_kategori(17), "Mildt")
        self.assertEqual(temperatur_kategori(22), "Varmt")

    def test_nan(self):
        df = pd.DataFrame({"vind" : [np.nan, 2, 4]})
        df["vind"] = df["vind"].fillna(df["vind"].mean())
        self.assertFalse(df["vind"].isnull().any())
        self.assertAlmostEqual(df["vind"].iloc[0], 3.0) #(2+4)/2 = 3.0

    def test_statistikk(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(np.mean(data), 3)
        self.assertEqual(np.median(data), 3)
        self.assertAlmostEqual(np.std(data), 1.414, places=3)

    def test_unormal_hopp_temp(self):
        self.assertTrue(unormalt_hopp_temp(21), "For høyt hopp i temperatur, ikke logisk")
        self.assertFalse(unormalt_hopp_temp(5), "OK")

    
    def test_kategoriserer_trykk(self):
         self.assertEqual(kategoriserer_trykk(1018), "Høytrykk") 
         self.assertEqual(kategoriserer_trykk(1005), "Lavtrykk")

    def test_kategoriser_nedbør(self):
        self.assertEqual(kategoriserer_nedbor(0), "Tørt")
        self.assertEqual(kategoriserer_nedbor(3), "Våt luft")
        self.assertEqual(kategoriserer_nedbor(12), "Mye regn")
        self.assertEqual(kategoriserer_nedbor(25), "Ekstremvær")


#Ekstra test for ekstremalverdier
class TestEdgeTilfeller(unittest.TestCase):
    def test_hopp_nan(self):
        self.assertFalse(unormalt_hopp_temp(np.nan))
    
    def test_trykk_grensa(self):
        self.assertEqual(kategoriserer_trykk(1013), "Lavtrykk") #tester for eksakte grensa
    
    def test_nedbor_grensa(self):
        self.assertEqual(kategoriserer_nedbor(5), "Mye regn") #genrese mellom våt luft og mye regn
        self.assertEqual(kategoriserer_nedbor(20), "Ekstremvær") #grense mellom mye regn og ekstramvær

if __name__ == '__main__': 
    unittest.main()