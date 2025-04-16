def kategoriser_data(df):
    #kategoriserer temperaturen
    df["TemperaturKategori"] = ["Kaldt" if temp2 < 10
                            else "mildt" if temp2 < 20 
                            else "varmt" for temp2 in df["Temperatur (°C)"]
                            ]

    #kategoriserer vind
    df["VindKategori"] = ["Vindstille" if vind2 < 2
                      else "Lett bris" if vind2 < 10
                      else "Sterk vind" if vind2 < 20
                      else "Storm" for vind2 in df["Vindhastighet (km/t)"]]

    #kategoriserer trykk
    df["TrykkKategori"] = ["Høyttrykk" if trykk2 > 1013
                       else "Lavtrykk" for trykk2 in df["Trykk"]]

    #kategoriserer nedbør
    df["NedborKategori"] = ["Tørt" if nedbor2 == 0
                        else "Lett regn" if nedbor2 < 5
                        else "Mye regn" if nedbor2 < 20
                        else "Ekstrem vær" for nedbor2 in df["Nedbør (mm)"]]
    return df