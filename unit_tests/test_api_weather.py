import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import pandas as pd
import sys
import os

# Legg til riktig path til src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importer funksjonen som skal testes
from Api_weather import hente_data_fra_api


class TestHenteDataFraAPI(unittest.TestCase):

    @patch("Api_weather.requests.get")
    def test_returnerer_dataframe(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "date": "2025-01-16",
                    "temperature": 2.5,
                    "pressure": 4.2,
                    "precipitation": 0.0
                }
            ]
        }
        mock_get.return_value = mock_response

        df = hente_data_fra_api("Trondheim", datetime(2025, 1, 16), datetime(2025, 1, 17))
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertIn("temperature", df.columns)

    @patch("Api_weather.requests.get")
    def test_tom_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": []}
        mock_get.return_value = mock_response

        df = hente_data_fra_api("Trondheim", datetime(2025, 1, 16), datetime(2025, 1, 17))
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)

    @patch("Api_weather.requests.get")
    def test_feilrespons(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Not found"}
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            hente_data_fra_api("Ugyldig", datetime(2025, 1, 16), datetime(2025, 1, 17))


if __name__ == '__main__':
    unittest.main()
