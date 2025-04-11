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