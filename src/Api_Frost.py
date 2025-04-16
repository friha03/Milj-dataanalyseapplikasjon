# Lage ny fil

import requests #http forespørsler
import pandas as pd


#sender GET forespørsel til API frost
def hent_frost_data(endpoint, parameters, client_id):
    r = requests.get(endpoint, params = parameters, auth=(client_id, None))
    #sjekker om GET forespørselen er vellykka
    #200=ok
    if r.status_code ==200:
        json_data = r.json() #konverterer til JSON format
        print("Data hentet fra Frost API")
        return json_data
    else: 
    #feilmelding og årsak 
        error_msg = r.json().get("error", {}).get("message", "Ukjent feil")
        error_reason = r.json().get("error", {}).get("reason", "Ingen grunn spesifert")
        raise ValueError(f"API-feil: {r.status_code}\nMelding: {error_msg}\nÅrsak: {error_reason}")

def frost_json_til_dataframe(json_data):
    #tom liste som lagrer observasjoner
    vaerdata = []
    #går gjennom data
    for entry in json_data.get("data", []):
        timestamp = entry.get("referenceTime", "Ukjent tidspunkt")
        observations = entry.get("observations", [])
        #ordbok for ei rad i datasettet
        weather_entry = {"Tidspunkt" : timestamp}
        for obs in observations: 
            element = obs.get("elementId", "Ukjent element")
            value = obs.get("value", "Ukjent verdi")
            weather_entry[element] = value
        #legger rad til i lista
        vaerdata.append(weather_entry)

    #Pandas Dataframe i lista med observasjonene
    df = pd.DataFrame(vaerdata)
    #fjerner radene der verdiene er NaN ikke tidspunkt
    df.dropna(how = "all", subset=df.columns[1:], inplace=True)
    #CSV fil
    return df

def lagre_til_csv(df, filnavn):
    df.to_csv("trondheim_vaerdata_full.csv", index = False, encoding="utf-8")
    print("data lagret i trondheim_vaerdata_full.csv")





#HÅNDTERING AV UREGELMESSIGHETER
def rense_data(df):
    
    #værdata som kan være feilmålinger, som ekstreme temperaturer osv, plutselig hopp
    #bort med usansynlige temperaturer
    df = df[(df["mean(air_temperature P1D)"] > -50) & (df["mean(air_temperature P1D)"] < 50)]
    #fjerner negative verdier for nedbør og ekstreme verdier
    df  = df[(df["sum(precipitation_amount P1D)"]>=0) & (df["sum(precipitation_amount P1D)"]<100)]
    #fjerner negative og ekstreme verdier
    df = df[(df["mean(wind_speed P1D)"]> 0) & (df["mean(wind_speed P1D)"]< 45)]

    #erstatter åpenbare feil med NaN
    df.replace(-9999, None, inplace=True)

    #temperaturhopp
    df["TempDiff"] = df["mean(air_temperature P1D)"].diff() #beregn differansen mellom hver måling
    df["UnormalHoppTemp"] = df["TempDiff"].apply(lambda x: "Ja" if abs(x) > 10 else "Nei") #Markerer plutselige endringer med Ja eller nei

    #Trykkhopp
    df["PressureDiff"] = df["mean(air_pressure_at_sea_level P1D)"].diff() #differanse mellom hver måling
    df["UnormalHoppPressure"] = df["PressureDiff"].apply(lambda x: "Ja" if abs(x) > 100 else "Nei") #Markerer plutselige endringer

    #vindhopp
    df["Wind_speedDiff"] = df["mean(wind_speed P1D)"].diff()  #differanse mellom hver måling
    df["UnormalHoppWind"] = df["Wind_speedDiff"].apply(lambda x: "Ja" if abs(x) > 10 else "Nei") #Markerer plutselige endringer

    #nedbørhopp
    df["NedborDiff"] = df["sum(precipitation_amount P1D)"].diff()  #differanse mellom hver måling
    df["UnormalHoppNedbor"] = df["NedborDiff"].apply(lambda x: "Ja" if abs(x) > 10 else "Nei") #Markerer plutselige endringer

    return df
