Værdata analyse for Trondheim 2020-2025

# INTRODUSKJON

I denne mappa henter vi inn ulike værdata fra API_Weather fra februar til mars i 2025. Vi behandler deretter dataen, renser den, fjerner feil verdier / verdier out of range, og lager ulike plot. Vi kategoriserer dataen som temperatur, vind, nedbør og trykk. Vi skal se på ulike temperaturer, derav de varmeste dagene, med minst vind og lite nedbør, når det egner seg å bade. I denne filen ser vi på alle lørdager kl 10:00, og sammenligner disse.


## FUNSKJONALITET

- Importerer nødvendige biblioteker
- Laster inn API-nøkkel og endepunkt med .env-filen, som sikrer at sensetive opplysninger ikke eksponeres i koden
- Henter data og lagrer som CSV-fil ved navn trondheim_vaerdata_full_1.csv. Vi velger værparametrene lufttemperatur, luffttrykk, vindhastighet og nedbør.
- Renser data, og fjerner feil målinger, som ekstreme tilfeller
- Legger i kategoriene temperatur, trykk, nedbør og temperatur. Henter deretter ut for kl 10:00 hver lørdag 
- Statistiske analyser: gjennomsnitt av alle lørdager, median, standardavvik
- Plot
- Spørringer med Pandas. I denne mappen valgte vi å bruke pandas fremfor pandasql da vi ønsket å kunne sammenligne de to ulike håndteringene. Pandas er mer effektivt og fleksibelt, og kan håndere mange rader raskere enn pandasql. I tillegg har det et større sett med funksjoner, med innebygde metoder for dataanalyse og datarensning . Det er også mer minneeffektivt, og jobber direkte med DataFrame
- Kategoriserer værdataen med "Kaldt", "Ekstremvær" osv
- Deretter henter vi ut de dagene med best bade-vær lite vind, nedbør og varmt, og plotter dette
- statiske analyser
- Visualiserer verdier med plot i form av Matplotlib og Seaborn
- Pandas og PandasQL
- Lager en predektiv analyse med en lineær regresjon som kan forutsi været i 2026 basert på tidligere data for temperaturer, dette ble noe mere utfordrende her i og med at vi hadde lite data å ta utgangspunkt i. 
- Visualiserer faktiske verdier i forhold til predikerte verdier


## Struktur

- For å gjøre oppgaven mer strukturert og forståelig har vi brukt src filer
- API_Weather.py tilhører kode som kun ligger i dette API et, og henter ut data renser den og konverterer til JSON format
- plot_funksjon.py, statisk_maal.py og predikasjon.py tilhører begge APIene
- plot_funksjoner innholder koden til plottene i 2D og 3D format
- statisk_maal er utregningene på gjennomsnitt, median og standaraavik
- predektive modeller er funksjoner som bruker lineær regresjon og predikerer været
- API_Frost.py har vi lagt inn try, except blokker for å sjekke at det ikke er nettverksfeil ved henting av JSON


## Forhindre feil

- Try, except blokker i src filen, som håndterer nettverksfeil, JSON formarteringsfeil eller ugyldige API parametere
- Enhetstester, der test_verdi_data.py og verdi_data.py tilhører Frost API
- test_verdi_data_py tester logikk for uregelmessige hopp i de ulike vær parameterene, og ekstreme tilfeller
- verdi_data.py er funksjoner som kategoriserer


## Versjonshåndtering og sammerbeid

- Bruker Git aktivt, holder da oversikt
- brancher, og commit meldinger
- .gitignore sikrer at .env lastes opp
