import requests
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
api_key_1 = os.getenv('API_KEY_1') #Gjør dette med enn .env fil
print(api_key_1)
base_URL = os.getenv('DATABASE_URL')

def hente_data_fra_api(city: str, start_date: datetime, end_date: datetime):
    vaerdata = []

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        url = f"{base_URL}/history.json?key={api_key_1}&q={city}&dt={date_str}"


        response = requests.get(url)

        if response.status_code == 200: #Kontroll for vellykket API-kall
            data = response.json()
        else: 
            print(f"Feil ved henting av data fra API-et for {date_str} : {response.status_code} ")
            current_date += timedelta(days=1)
            continue


        for hour_data in data.get("forecast", {}).get("forecastday", [])[0].get("hour", []):
            tidspunkt = hour_data.get("time", "Ukjent tidspunk")
            temperatur = hour_data.get("temp_c", "Ukjent temperatur")
            vindhastighet = hour_data.get("wind_kph", "Ukjent vindhastighet")
            pressure_mb = hour_data.get("pressure_mb", "Ukjent trykk" )
            nedbør = hour_data.get("precip_mm", "Ukjent nedbør")

            vaerdata.append({
                "Tidspunkt" : tidspunkt, 
                "Temperatur (°C)" : temperatur, 
                "Vindhastighet (km/t)" : vindhastighet,
                "Trykk" : pressure_mb, 
                "Nedbør (mm)" : nedbør
            })

        current_date += timedelta (days=1)
        df = pd.DataFrame(vaerdata)
        return df 
        