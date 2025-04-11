# Refleksoner over hva du har lært om datainnsamling, databehandling, dataanalyse og visualisering.
 Jeg har fått mer forståelse over hva databehandlig er og hvordan dette kan brukes. En av de vikstigste erfaringene fra prosjektet var å arbeide med åpne datakilder. Jeg har erfart hvordan man kan sikre at APIen er pålitelig og relevant. Ved behandlingen av dataen har vi renset ut feil, som manglende verdier. Vi har også strukturert datene som Pandasql i tabeller. Dette var en metode som skapte god oversikt over store mengder data på en effektiv måte. Vi har benyttet funksjoner som .interpolate() og .mean() for å behandle og omforme datasettet til formater bedre tilegnet analyse.

# Beskrivelse av nye ferdigheter som ble tilegnet, for eksempel bruk av spesifikke biblioteker (Pandas, NumPy, Matplotlib, etc.) og programmeringskonsepter.

Jeg har fått erfaring med flere viktige verktøy og biblioteker som er sentrale i datavitenskap.Biblioteket pandasql, som gjorde hentingen av ulike datafreams i pandas enkelt, har vært nyttig. En ny og viktig erfaring er også å bruke koder som er gjenbrukbare i form av source, for å gjøre koden kortere og mer strukturert. I tillegg lærte jeg å skrive enhetstester med unittest, noe som var nytt for meg. Dette bidro til å sikre at funskjonene våre fungerte som forventet, i tillegg til å oppdage feil tidlig. En annen ting er bruk av Git og GitHub til versjonskontroll. Vi har brukt separate grener for ulike funskjoner for å kombinere endringene våre

# Identifisering av spesifikke utfordringer som oppstod under prosjektet, for eksempel problemer med datakvalitet, håndtering av manglende verdier, eller tekniske problemer med API-er.

Vi har brukt mye tid og innsats på å hente ut API med nok og riktig data, som vi i tillegg kunne få tilgang til. Flere av APIene vi prøvde gikk også ut på dato, sli kat vi måtte registrere oss flere ganger. Vi slet også litt med kompilering av GIT. Vi hadde ingen mangler av verdier i APIene vi til slutt endte opp med, og måtte derfor legge inn feil selv.

# Refleksjoner over samarbeidet i gruppen, inkludert hvordan oppgaver ble fordelt og hvordan kommunikasjonen fungerte.
Jeg syns samarbeidet i gruppa har fungert godt. Alle har vært like ivrige, og jobbet godt sammen. Vi har hatt litt problemer med å finne tid til å møte opp i øvingstimene som har vært satt opp, da det har krasjet med andre fag. I tillegg har jeg måttet gjennomgå en kneoperasjon midt i prosessen, som har ført til mye jobbing over teams. Men til tross for dette syns jeg vi har klart å fordele oppgavene godt, og alle på gruppa har bidratt like mye. 
...

# Vurdering av de endelige resultatene, inkludert kvaliteten på visualiseringene og analysene.

Vi endte opp med to fungerende applikasjoner, som begge tar for seg værendringene i Trondheim. Det ene over fem år, det andre over de påbegynte månedene av 2025. I begge APIene har vi renset sett på værendringene over tid, både de varmeste dagene temperaturmessig, men også dagene med minst vind, nedbør og luftfuktighet. Vi har lagd flere plots av data og resultater. Vi produserte visualiseringene med Plotly og Mtplotlib, og brukte blant annet scatterplots og tidsseriediagrammer. Fra disse så vi at blant annet temperatur og nedbør svingte naturlig med årstidene, så dataene så ut til å stemme godt med virkeligheten. Da vi skulle vi skulle prediktere fremtiden fikk en lineær regresjon som ikke ga mening. Men ordnet dette med å ta regresjon av hver enkelt dag i en liste. Noe som ga mer riktige resultater for 2026. Kvaliteten på datene er god i og med at vi ikke har noen feil, men håndterer det som om det er feil. Vi viser også at dette fungerer i egen fil. Kildene våre er også pålitlige da de de begge er kvalitetssikrede og følger internasjonale standarder. 

# Ideer til hvordan prosjektet kan forbedres i fremtiden, både i forhold til tekniske aspekter og prosjektledelse.

Prosjektet kan forbedres med å hente data fra lengre tid tilbake i tid. Dette vil forbedre regresjon og predektiv analyse. Ved å hente data fra lengre tilbake i tid vil vi også få mere oversikt over endringer gjennom tiden, samt flere år å hente data for enkelte dager for å predikerer en sammenheng med den globale oppvarmingen. Vi kunne også hatt en mer oversiktlig applikasjon, med enda tydeligere navn i kodene. 

# Mulige retninger for videre forskning eller utvikling basert på erfaringene fra prosjektet.

Hadde vi hentet data fra lengre bak i tid kunne vi sett på klimaendringene, hvordan nedbør og temperatur endrer seg med økte utslipp. Predikerer hvordan dette vil fortsette å utvikle seg i forhold til hvordan utslippene utvikler seg. Vi kunne også gått videre med å sammenlige de to APIene våre. 

# Oppsummering av de viktigste læringspunktene og hvordan prosjektet har bidratt til studentenes forståelse av datavitenskap og miljøstudier.

Jeg har lært hvordan man håndterer veldig store sett med data. Hvordan man kan strukturere dette og kun hente ut det nødvendige. At antall linjer med data ikke nødvendigvis trenger å være overveldende, bare man vet hvordan man skal håndtere det. Har også lært hva en API adresse er, hvordan man tar den i bruk og hvordan man henter ut det innholdet vi er intressert i. Har også lært hvordan en API Key fungerer. At man må lagre denne i en. env fil for å ikke publisere denne når vi pusher til git, slik at alle får tilgang til API adressen. I sin helhet har prosjektet gitt meg forståelse av hvordan data kan hentes inn, analyseres og videreformidles på en strukturert måte, og hvordan dett ean brukes til viktige samfunnsutfordringer, som foreksempel klimaendringer. 

# Personlige tanker om hvordan erfaringene fra prosjektet kan anvendes i fremtidige studier eller yrkesliv.

Jeg tenker at erfaringene fra prosjektet har gitt meg nyttige verktøy jeg kan ta med meg i både studier og arbeidsliv. Som student på Energi og Miljø ser jeg stor verdi i å kunne bruke verktøy som Python og Pandas til å analysere energiforbruk, utslipp og værdata. Det er også nyttig å kunne hente ut og behandle data fra åpne kilder. Prosjektet har vist meg hvor viktig det er å kunne kombinere teknologiske verktøy med forståelse fra miljøfag. 