import requests #HTTP kall
import pandas as pd #lagre i dataframe
from datetime import datetime, timedelta
import os #miljøvariabler
from dotenv import load_dotenv #laste env fila

load_dotenv() #miljøvariabler blir lasta opp fra env fil

api_key_1 = os.getenv('API_KEY_1') #API key
base_URL = os.getenv('DATABASE_URL') #URL

#feil om noko mangler
if not api_key_1 or not base_URL:
    raise ValueError("Databasen eller API key mangler i env fila")

#city er navnet på byen, pluss intervall for henting av dataen
def hente_data_fra_api(city: str, start_date: datetime, end_date: datetime):
    if start_date > end_date:
        raise ValueError("Startdatoen må komme før sluttdato.")

    vaerdata = [] #tom liste

    current_date = start_date #start er dagens dato
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d") #dato til formatet år, måned dag
        url = f"{base_URL}/history.json?key={api_key_1}&q={city}&dt={date_str}"

        response = requests.get(url) #kaller på API

        if response.status_code != 200:
            raise ValueError(f"Feil når vi skal hente data fra {date_str}: {response.status_code}")

        data = response.json() #svaret leses som en JSON

        # Sjekker om det er data for dagen
        forecast_days = data.get("forecast", {}).get("forecastday", [])
        if not forecast_days:
            current_date += timedelta(days=1)
            continue

        for hour_data in forecast_days[0].get("hour", []):
            tidspunkt = hour_data.get("time")
            temperatur = hour_data.get("temp_c")
            vindhastighet = hour_data.get("wind_kph")
            pressure_mb = hour_data.get("pressure_mb")
            nedbør = hour_data.get("precip_mm")

            #lagrer på ei rad
            vaerdata.append({
                "Tidspunkt": tidspunkt,
                "Temperatur (°C)": temperatur,
                "Vindhastighet (km/t)": vindhastighet,
                "Trykk": pressure_mb,
                "Nedbør (mm)": nedbør
            })

        current_date += timedelta(days=1) #videre til ein ny dag

    return pd.DataFrame(vaerdata)
