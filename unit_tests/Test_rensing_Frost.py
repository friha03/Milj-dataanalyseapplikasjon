import unittest
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from Api_Frost import rense_data


class TestRensingFrost(unittest.TestCase):
    def setUp(self):
        # Lager et lite datasett med noen feilverdier
        self.df = pd.DataFrame({
            "mean(air_temperature P1D)": [12, 52, -63, 5],
            "mean(air_pressure_at_sea_level P1D)": [1011, 940, 1200, 1000],
            "mean(wind_speed P1D)": [3, 60, -15, -2],
            "sum(precipitation_amount P1D)": [0, -10, 150, 50]
        })

    def test_rensing_fjerner_outliers(self):
        df_renset = rense_data(self.df)

        # sjekk om det berre er ei rad igjen etter rensinga
        self.assertEqual(len(df_renset), 1)

        # Sjekk på om unormale kolonna nå eksisterer
        self.assertIn("UnormalHoppTemp", df_renset.columns)
        self.assertIn("UnormalHoppPressure", df_renset.columns)
        self.assertIn("UnormalHoppWind", df_renset.columns)
        self.assertIn("UnormalHoppNedbor", df_renset.columns)

        # Sjekk på at vi ikkje har noken -9999 verdi
        self.assertFalse((df_renset == -9999).any().any())

if __name__ == '__main__':
    unittest.main()
