import requests #HTTP
import pandas as pd #dataframe
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv() #laster inn data

api_key_1 = os.getenv('API_KEY_1') #api
base_URL = os.getenv('DATABASE_URL')#URL

#stopper hele koden om api eller url ikke finnes
if not api_key_1 or not base_URL:
    raise ValueError("Database eller API key mangler i fila")
#stedet vi finner data og intervall
def hente_data_fra_api(city: str, start_date: datetime, end_date: datetime):
    if start_date > end_date: #feil om datoene ikke gir logisk meining
        raise ValueError("Startdato må være før sluttdatoen.")

    vaerdata = [] #tom lista

    current_date = start_date #dagens dato er start dage
    while current_date <= end_date: #iterer seg gjennom til siste dag
        date_str = current_date.strftime("%Y-%m-%d")
        url = f"{base_URL}/history.json?key={api_key_1}&q={city}&dt={date_str}"

        response = requests.get(url) #HTTP forespørsel

        if response.status_code != 200:
            raise ValueError(f"Feil når vi henter dataen {date_str}: {response.status_code}")

        data = response.json() #leser JSON som en Python ordbok

        # Går gjennom hver time i den dagen
        for hour_data in data.get("forecast", {}).get("forecastday", [])[0].get("hour", []):
            tidspunkt = hour_data.get("time") #tidspunkt
            temperatur = hour_data.get("temp_c") # celius som temperatur
            vindhastighet = hour_data.get("wind_kph")# km/t som vind
            pressure_mb = hour_data.get("pressure_mb") # hPa i lufttrykk
            nedbør = hour_data.get("precip_mm") # mm som nedbør

            vaerdata.append({
                "Tidspunkt": tidspunkt,
                "Temperatur (°C)": temperatur,
                "Vindhastighet (km/t)": vindhastighet,
                "Trykk": pressure_mb,
                "Nedbør (mm)": nedbør
            })

        current_date += timedelta(days=1) #neste dag

   
    df = pd.DataFrame(vaerdata)
    return df
