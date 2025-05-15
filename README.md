# OPPGAVENS HOVEDSTRUKTUR

## Generelt
I denne oppgaven har vi valgt å hente ut miljødata fra to ulike API'er. Både fra API weather og API Frost. API_Frost mappen inneholder to filer. En som sørger selve databehandlingen, og en som legger til feil for å sjekke at behandlingen faktisk fungerer. API-Weather inneholder API_henting _fra_Weather, Dataanalyse_visualiseringer, Databehandling_av_Weather_API, Prediktiv_analyse_for_Westher_API. I begge to henter vi ut og behandler værdata fra Trondheim. Spesifikt temperatur, nedbør, trykk og vindhastighet.  


## API-Frost
### databehandling
I databehanling-mappen starter vi med å hente ut CSV og lagrer værdata fra 2020 til og med mars 2025. Deretter håndteres manglende verdier, værdataen kategoriseres med lister. Vi filtrerer så dagene med finest vær med SQL-spørringer i Pandas. Dataene visualiseres med scatterplots og 3D. I del 2 tar vi statisk datanalyse av værmålinger, korrelasjonsanalyse og sammenhenger mellom temperatur og trykk, mellom temperatur og vindstyrke, og mellom varme, tørre og vindstille dager. I tillegg viualisering av værparametre over tid, av både trykk, temperatur, vind og nedbør. Predikasjonen fra dette API-et handler om å forutsi neste dags temperatur med lineær regrasjon, visualisering og linjediagram av faktisk og predikert temperatur. Vi ser også på feilen mellom faktisk og predikert temperatur, og modellerer predikert vær. 

### Lage feil i CSV
Lage_feil_i_CSV oppretter feil i API-et for å så legge tilbake faktiske verdier. Dette gjøres for å sjekke at databehandlingskodene fungerer optimalt. 


## API-Weather
### API_henting _fra_Weather
I API_henting _fra_Weather hentes og lagres data fra APIet. 

### Dataanalyse visualiseringer
I Dataanalyse_visualiseringer filtreres data til å inneholde data fra lørdager klokken 10:00, finner dataen der isbading egneer seg best med Pandas og Pandasql, plotter i 2D og 3D med scatterplot, sammenligner med seaborn. Plotter også de ulike parametrene hver for seg og sammenligner disse. 

### Databehandling av Weather_API
Databehandling_av_Weather_API strukturerer og behandler dataten, henter data fra CSV, sammenligner med Pandasql, og behandler nan-verdier. 

### Prediktiv analyse for Weather_API
Prediktiv_analyse_for_Westher_API predikterer data for fremtiden med regresjon og trening. 


## Source
Inneholder koder som blir brukt i både API_weather og API_Frost. Source-filene API_Frost og API_Weather inneholder kun koder til de spesifikke API-ene. Kategorisering, plot_funksjon, predikasjon, statisk_maal inneholder koder som begge API-ene kan bruke. 

## Unit tests
Unit_tests inneholder filene test_api_weather, test_rensing_Frost, test_verdi_data, verdi_data. Her testes de største og viktisgste kodene, for å se om de fungerer slik de skal. 