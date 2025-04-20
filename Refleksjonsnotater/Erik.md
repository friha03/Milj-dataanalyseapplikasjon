# Refleksoner over hva du har lært om datainnsamling, databehandling, dataanalyse og visualisering.
Gjennom dette prosjektarbeidet har jeg fått en dypere forståelse for hvordan man kan hente inn og bearbeide data fra forskjellige kilder ved hjelp av API-er. Jeg har lært å skille mellom åpne datakilder som er fritt tilgjengelig, og datakilder som krever registrering og bruke av API-nøkler for å få tilgang til og hente ut data. Dette tror jeg kommer til å bli en verdifull kunnskap for fremtidige prosjektoppgaver i både studie og jobbsammenheng. 

Når det gjelder databehandling, har jeg gjennom prosjektarbeidet lært at man bør importere og bruke biblioteker som pandas og pandasql, for å strukturere, filtrere og endre på dataen man tar inn. Dataen bør man organisere i DataFrame-strukturer for å gjøre den lettere å anylsere og jobbe videre med. For bedre struktur og forståelse av datasettet, lønner det seg også å kategorisere dataen man har hentet inn i underkategorier. Til dette har jeg lært at list comprehension er et nyttig verktøy. 

For dataanalyse og visualiseringer har jeg i dette prosjektet lært om scatterplott, som er et nyttig verktøy når man vil plotte to verdier opp mot hverandre for å finne korrelasjon. Ellers har vi brukt plot struktur fra matplotlib og numpy, som vi tidligere har lært om i blant annet IT-GK. Derimot har jeg opparbeidet meg en bredere forståelse ved å bruke plottene aktivt i dette prosjektet.


# Beskrivelse av nye ferdigheter som ble tilegnet, for eksempel bruk av spesifikke biblioteker (Pandas, NumPy, Matplotlib, etc.) og programmeringskonsepter.
Dette prosjektarbeidet har gitt meg en større innsikt av hvordan man bør strukturere større dataprosjekter med mapper og hvilke filer som bør ligge under mappa. Eksempelvis en sorce-mappe der man definerer funksjonsene, data-mappe der man samler csv- og json-filer og unit_test-mappe for enhetstester. Videre har jeg fått en praktisk erfaring av hvordan man kan bruke et versjonskontrollsystem som GitHub, til å sammarbeide godt med andre utviklere på et prosjekt. 

I tillegg har jeg i løpet av prosjektoppgaven fått kjennskap til flere andre biblioteker som jeg ikke har vært borte i før. For eksempel har jeg lært om missingno som raskt kontrollerer feil/mangler i datasettet, sklearn som kan brukes til å predikere data og pandasql som vi har brukt i databehandlingen.


# Identifisering av spesifikke utfordringer som oppstod under prosjektet, for eksempel problemer med datakvalitet, håndtering av manglende verdier, eller tekniske problemer med API-er.
Vi slet lenge med å finne noen API-er som fungerte å bruke. Og da vi først fant noen API-er som vi kunne hente inn i prosjektet, inneholdt de ikke, eller lite historisk data. Etter flere forsøk klarte vi å ende på to API-er som begge viser historisk data for Trondheim. Midtveis i prosjektet fikk vi problem med at API-keyen fra API Weather utløp, da tydeligvis registreringen her bare er tidsbestemt for en gitt periode. Dette løste vi med å registrer oss på ny, med en annen mail fra en annen på gruppa.

Ellers hadde vi problemer med versjonskontroll i GitHub i starten av prosjektet. På et tidspunkt klarte vi å slette alt arbeidet vi hadde gjort med det ene API-et. Heldigvis fikk vi hjelp til å hente opp en tidligere versjon via GitHub, som ga oss en nyttig læreopplevelse av hvordan man kan finne og gjenopprette tidligere commits vha. GitHub. Etterhvert som vi har jobbet med prosjektet har vi opparbeidet oss en bedre kunnskap om versjonshåndtering. Dette gjør at det har blitt mye enklere å pulle og pushe endringer nå, enn det var tidligere.


# Refleksjoner over samarbeidet i gruppen, inkludert hvordan oppgaver ble fordelt og hvordan kommunikasjonen fungerte.

Samarbeidet i gruppen vil jeg si har fungert veldig bra! Vi har valgt å jobbe fysisk sammen når vi har jobbet med prosjektet, som har gjort det enklere å håndtere feilmeldningene og utfordringer - særlig  knyttet til versjonskontroll, men også generelle tenkiske problemer som har oppstått underveis i prosjektet. Ellers har vi fordelt arbeidsoppgaver rettferdig, der hver enkelt har hatt ekstra ansvar for spesifikke deler av prosjektet. For eksempel har Silje og Frida jobbet mest med Frost API-et, mens jeg har jobbet mest med Weather API-et. Samtidig har vi alle jobbet på tvers av prosjektet, og hjulpet hverandre når det har trengtes. Dette har gjort at vi alle sammen fått en bred og helhetlig forståelse av prosjektet.

Kommunikasjonen synes jeg også at har fungert veldig bra. Til tross for at vi noen ganger har vært nødt til å jobbe over teams på grunn av skade og reise, synes jeg vi har klart å opprettholde en god flyt i prosjektet. Det har nok hjulpet at vi alle tre studerer samme studie og går i samme klasse, når det har kommet til planlegging av felles tidspunkter for å jobbe med prosjektet. Alt i alt er jeg veldig fornøyd med gruppa, og hvordan vi har jobbet sammen om prosjektet!


# Vurdering av de endelige resultatene, inkludert kvaliteten på visualiseringene og analysene.
Jeg synes vi har fått oversiktlige resultater, med god kvalitet på visualiseringene. Som problemstilling for prosjektet, valgte vi å undersøke datoer som har vært velegnet for bading/isbading. For Frost API-et endte vi med at det har vært 19 velegnede dager for bading, mens Weather API-et fikk ut at det har vært fem velegnede lørdager (kl. 10) for isbading. Dataanalysen ga at ingen av de to API-ene hadde særlige feil/mangler i datasettene. Derfor valgte vi å lage vår egen CSV-fil som vi la inn feil i, slik at vi fikk vist hvordan vi kan håndtere feil i datasett.


# Ideer til hvordan prosjektet kan forbedres i fremtiden, både i forhold til tekniske aspekter og prosjektledelse.
(Tolker spørsmålet som hvordan prosjektoppgaven i faget kan utvikles for fremtiden)

Jeg tror at man tidligere bør komme i gang med undervisningen knyttet direkte til prosjektet. Vi opplevde det som utfordrende at da vi startet med prosjektarbeidet, hadde vi ikke lært noe særlig om hva et API var, ei heller hvordan man kunne bruke API-er. Generelt i prosjektet har man sittet med en følelse at man har måtte lære seg innhold, før man har fått noe teoretisk gjennomgang av det. Prosjektet er også ganske omfattende, som har gjort det krevende å jobbe med, i form av at det har tatt mange arbeidstimer.

Til en annen gang tror jeg også det hadde vært lurt å gjøre noen av de to øvingene til samarbeidsoppgaver, eller på en eller annen måte fått implementert versjonskontroll for flere utviklere sammen, tidlig i semesteret. For det er noe som i hvert fall for vår del, har tatt mye tid å lære seg.


# Mulige retninger for videre forskning eller utvikling basert på erfaringene fra prosjektet.
For vårt prosjekt kunne vi ha hentet inn flere datakilder fra uavhengige kilder, og sammenlignet forskjellige verdier. For eksempel kunne vi ha hentet inn et API som viser sanntidsdata for Trondheim, og sammenlignet dette med de predikerte verdiene vi har fått fra Frost API. Dette ville gitt oss en innsikt av hvor presise værmodellen vår hadde vært i praksis. 

Ellers er det mange flere spennende retninger som vi hadde kunne gjort for å videreutviklet og forbedret prosjektet vårt. Jo mer vi har jobbet sammen med prosjektet, jo flere tanker har vi fått mtp hva som vi kan gjøre for å forbedre og effektivisere programmet vårt! Samtidig må det nevnes at vi har begrenset tid til rådighet, og andre emner som vi også må jobbe med, noe som gjør at man må sette noen grenser for hvor mye man kan finpusse og vidreutvikle et program.


# Oppsummering av de viktigste læringspunktene og hvordan prosjektet har bidratt til studentenes forståelse av datavitenskap og miljøstudier.
Prosjektet har bidratt til å gi meg en god forståelse for hvordan man kan hente inn, analysere og videreutvikle data ved hjelp av API-er. I tillegg har jeg fått en forståelse for hvordan man kan bruke den innsamlede dataen til å gjøre prediksjoner for fremtidige trender og utvikling. I vårt tilfelle har vi bare hentet inn værdata fra fem år tilbake i tid, noe som har gitt oss et innblikk i værmønstre, men ikke nødvendigvis et tydelig bilde på hvordan klimaet har endret seg over tid. 

Dersom vi derimot hadde brukt et API som ga tilgang til historisk data over en periode på førti år tilbake i tid eller mer, ville vi hatt et bedre grunnlag for å analysere klimaendringer. Ved bruk av samme analysemetoder som vi har brukt i dette prosjektet, kunne vi da for eksempel ha undersøkt utviklingen av gjennomsnittstemperatur over tid, og deretter brukt resultatene som utgangspunkt til å predikere hvordan temperaturen kan utvikle seg de neste 15 åra. Dette tror jeg ville ha vært svært anvendtbart for videre miljøstudier!


# Personlige tanker om hvordan erfaringene fra prosjektet kan anvendes i fremtidige studier eller yrkesliv.
Jeg tror at jeg kommer til å ta med meg mye av det vi har gjennomgått i dette prosjektet i både fremtidige studier, men også i arbeidslivet. Prosjektet har gitt meg en grunnleggende forståelse for hvordan man kan samarbeide effektivt i et utviklingsteam, og hvordan man bør strukturere og organisere et programmeringsprosjekt. Denne erfaringen tror jeg kommer godt til nytte i kommende emner som krever programmeringsevner, og eventuelt også master oppgaven, når den tid kommer. 

Ellers tror jeg at den kunnskapen til å hente inn analysere og bearbeide data fra eksterne datakilder kommer til å være veldig nyttig og ettertraktet når man kommer ut i arbeidslivet. 