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
    

class Test_Data(unittest.TestCase): 
    def test_Kategori(self): 
        self.assertEqual(temperatur_kategori(-2), "Kaldt")
        self.assertEqual(temperatur_kategori(17), "Mildt")
        self.assertEqual(temperatur_kategori(22), "Varmt")

    def test_nan(self):
        df = pd.DataFrame({"vind" : [np.nan, 2, 4]})
        df["vind"].fillna(df["vind"].mean(), inplace=True)
        self.assertFalse(df["vind"].isnull().any())
        self.assertAlmostEqual(df["vind"].iloc[0], 3.0) #(2+4)/2 = 3.0

    def test_statistikk(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(np.mean(data), 3)
        self.assertEqual(np.median(data), 3)
        self.assertAlmostEqual(np.std(data), 1.414, places=3)

if __name__ == '__main__': 
    unittest.main()

