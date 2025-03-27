Værdata analyse for Trondheim 2020-2025

#INTRODUSKJON

I denne mappa henter vi inn ulike værdata fra API_frost fra 2020-2025. Vi behandler deretter dataen, renser den, fjerner feil verdier / verdier out of range, og lager ulike plot. Vi skal se på ulike temperaturer, derav de varmeste dagene, med minst vind og lite nedbør, når det egner seg å bade. 


##FUNSKJONALITET
- Importerer nødvendige biblioteker
- Laster inn API-nøkkel og endepunkt med .env-filen, som sikrer at sensetive opplysninger ikke eksponeres i koden
- Henter data og lagrer som CSV-fil ved navn trondheim_vaerdata_full.csv. Vi velger værparametrene lufttemperatur, luffttrykk, vindhastighet og nedbør. Vi henter gjennomsnitt per dag. 
- Renser data, og fjerner feil målinger
- Legger i kategoriene temperatur, trykk, nedbør og temperatur
- Statistiske analyser: gjennomsnitt, median, standardavvik
- Plot
- Spørringer med Pandas SQL (sqldf)





