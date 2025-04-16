Værdata analyse for Trondheim 2020-2025

## INTRODUSKJON

I denne mappa henter vi inn ulike værdata fra API_frost fra 2020-2025. Den gir ut den daglige gjennosmnitts temperaturen, lufttrykk, nedbør og vind. Vi behandler deretter dataen, renser den, fjerner feil verdier / verdier out of range, og lager ulike plot. Deretter kategoriserer vi dataene som CSV der vi anvender Pandas og pandasql. Vi skal se på ulike temperaturer, derav de varmeste dagene, med minst vind og lite nedbør, når det egner seg å bade. 


## FUNSKJONALITET
- Importerer nødvendige biblioteker
- Laster inn API-nøkkel og endepunkt med .env-filen, som sikrer at sensetive opplysninger ikke eksponeres i koden
- Henter data og lagrer som CSV-fil ved navn trondheim_vaerdata_full.csv. Vi velger værparametrene lufttemperatur, luffttrykk, vindhastighet og nedbør. Vi henter gjennomsnitt per dag. 
- Renser data, og fjerner feil målinger
- Legger i kategoriene temperatur, trykk, nedbør og temperatur
- Statistiske analyser: gjennomsnitt, median, standardavvik
- Plot
- Spørringer med Pandas SQL (sqldf)
- Kategoriserer værdataen med "Kaldt", "Ekstremvær" osv
- Deretter henter vi ut de dagene med best bade-vær lite vind, nedbør og varmt, og plotter dette
- Lager en predektiv analyse med en lineær regresjon som kan forutsi været i 2026 basert på tidligere data for temperaturer
- Visualiserer faktiske verdier i forhold til predikerte verdier

## Struktur
- For å gjøre oppgaven mer strukturert og forståelig har vi brukt src filer
- API_Frost.py tilhører kode som kun ligger i dette API et
- plot_funksjon.py, statisk_maal.py og predikasjon.py tilhører begge APIene
- plot_funksjoner innholder koden til plottene
- statisk_maal er utregningene på gjennomsnitt, median og standaraavik
- predektive modeller er funksjoner som bruker lineær regresjon og predikerer været
- API_Frost.py har vi lagt inn try, except blokker for å sjekke at det ikke er nettverksfeil ved henting av JSON

## Forhindre feil
- Ved å strukturere å ta ut feil i CSV filen brukte vi ulike koder, men vi hadde ingen feil
- Laget egen fil Lage_feil_i_CSV.ipynb har vi lagt inn egne feil og brukt koden i databehandling.ipynb for å vise at den fungerer til å rette opp feilene om vi hadde hatt dem i utgangspunktet
- Try, except blokker i src filen
- Enhetstester, der test_verdi_data.py og verdi_data.py tilhører Frost API

## Versjonshåndtering og sammerbeid
- Bruker Git aktivt, holder da oversikt
- brancher, og commit meldinger
- .gitignore sikrer at .env lastes opp






