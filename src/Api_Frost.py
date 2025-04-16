# Lage ny fil

import requests #http forespørsler
import pandas as pd


#sender GET forespørsel til API frost
def hent_frost_data(endpoint, parameters, client_id):

    try:
        r = requests.get(endpoint, params = parameters, auth=(client_id, None), timeout=10)
        r.raise_for_status() #HTTP error viss vi får en status ulik 200
        json_data = r.json() # forsøk på å dekode JSONet
        print("Vi har hentet data fra Frost API")
        return json_data
    except requests.exceptions.RequestException as e:
        print(f"Det oppsto en nettverksfeil når vi skulle hente ut data fra Frost API : {e}")
        return{} #tomt json blir returnert om vi har feil
    except ValueError as e:
        print(f"Klarte ikkje å lesa responsen av JSONet : {e}")
        return{}



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


