Værdata analyse for Trondheim 2020-2025

# INTRODUSKJON

I denne mappa henter vi inn ulike værdata fra API_Weather fra februar til mars i 2025. Vi behandler deretter dataen, renser den, fjerner feil verdier / verdier out of range, og lager ulike plot. Vi kategoriserer dataen som temperatur, vind, nedbør og trykk. Vi skal se på ulike temperaturer, derav de varmeste dagene, med minst vind og lite nedbør, når det egner seg å bade. I denne filen ser vi på alle lørdager kl 10:00, og sammenligner disse.


## FUNSKJONALITET
- Importerer nødvendige biblioteker
- Laster inn API-nøkkel og endepunkt med .env-filen, som sikrer at sensetive opplysninger ikke eksponeres i koden
- Henter data og lagrer som CSV-fil ved navn trondheim_vaerdata_full_1.csv. Vi velger værparametrene lufttemperatur, luffttrykk, vindhastighet og nedbør.
- Renser data, og fjerner feil målinger
- Legger i kategoriene temperatur, trykk, nedbør og temperatur. Henter deretter ut for kl 10:00 hver lørdag 
- Statistiske analyser: gjennomsnitt av alle lørdager, median, standardavvik
- Plot
- Spørringer med Pandas. I denne mappen valgte vi å bruke pandas fremfor pandasql da vi ønsket å kunne sammenligne de to ulike håndteringene. Pandas er mer effektivt og fleksibelt, og kan håndere mange rader raskere enn pandasql. I tillegg har det et større sett med funksjoner, med innebygde metoder for dataanalyse og datarensning . Det er også mer minneeffektivt, og jobber direkte med DataFrame
- Kategoriserer værdataen med "Kaldt", "Ekstremvær" osv
- Deretter henter vi ut de dagene med best bade-vær lite vind, nedbør og varmt, og plotter dette
- Lager en predektiv analyse med en lineær regresjon som kan forutsi været i 2026 basert på tidligere data for temperaturer, dette ble noe mere utfordrende her i og med at vi hadde lite data å ta utgangspunkt i. 
- Visualiserer faktiske verdier i forhold til predikerte verdier


