Værdata analyse for Trondheim 2020-2025

#INTRODUSKJON

I dette prosjektet hentes vi inn ulike værdata fra API fra 2020-2025. Vi behandler deretter dataen, renser den, fjerner feil verdier / verdier out of range, og lager ulike plot. Vi skal se på ulike temperaturer, derrav de varmeste dagene, med minst vind og lite nedbør, når det einer seg å bade. Vi henter ut data fra kl 00:00 hver dag.


#FUNSKJONALITET
- Henter data og lagrer som JSON/CSV
- Renser data, og fjerner feil målinger
- Legger i kategorier, som temperatur, trykk, nedbør og temperatur
- Statistiske analyser: gjennomsnitt, median, standardavvik
- Plot
- Spørringer med Pandas SQL (sqldf)



