# Dokumentasjon

## Hvordan bruke databasen:

1. Sørg for at du er i mappen databaser-db2.
2. Kjør filen `SetUpDatabase.py`. Dette vil sette opp databasen med all nødvendig informasjon.

   ```
    Python3 SetUpDatabase.py
   ```

3. Kjør filen `Main.py`. Dette vil starte programmet.

   ```
   Python3 Main.py
   ```

4. Følg deretter instruksjonene i terminalen.


**Merk:**

- Alle datoer for forestillinger må skrives på formen yyyy-mm-dd.
- Du kan ikke starte med å skrive mellomrom i terminalen når du velger hvilke deler av programmet du vil kjøre.
- Hvis du skal kjøre brukertilfelle 4 må brukertilfelle 2 være kjørt først for å få riktig antall solgte billetter til forestillingene.
- I brukstillfelle_2.py er vi klare over at read_hovedscene() leser feil stolernummer i galleri, men da alle disse var ledige (0) har det ikke noe å si
- Filen `tekstligeResultater.txt` viser hvordan en output kan være når man gjennomfører brukerhistoriens spørringer.
- Trønder 1, Trønder 2 og Baard Bratte har blitt lagt til som skuespiller i alle aktene. Disse rollene var oppgitt på hjemmesiden til TrøndelagTeater, men ikke i tabellen vi fikk i prosjektoppgaven.

**Eksempeldata som kan brukes til å teste databasen:**
- Dato: 2024-02-03
- Skuespiller: Emil Olafsson

## Endringer i databasen gjort etter DB1:

- **Klokkeslett**: Dropper klokkeslett i databasen siden alle forestillinger som viser samme stykke starter samtidig.

- **RolleIAkt**: Har rettet opp en feil og lagt til StykkeID til forskjell fra innlevering 1. Dette er for å kunne identifisere forskjellen på de to forskjellige stykkene.

- **RolleBesetning**: Har lagt til StykkeID for å lettere kunne hente ut data relatert til brukstilfelle 5. Vi kunne klart oss uten StykkeID og hentet ut stykke med kompliserte JOIN-setninger i SQL-spørringen. Likevel synes vi at den aktuelle spørringen ble mer intuitiv på denne måten.

- **Organisering av billettabeller**: Vi fjerner tabellene BillettType og BillettForestilling, til fordel for en enkel Billett-tabell. Tidligere var begge tabellene, BillettType og BillettForestilling, på 4. NF. Etter nærmere arbeid med databasen har vi innsett at det er mindre fordelaktig å ha to tabeller på 4. NF, fremfor én tabell som gjør databasen enklere å bruke.

- **NULL-verdi**: Har på enkelte tabeller lagt til muligheten til å ha nullverdi for ikke-nøkkelattributter. Tidligere var det ikke mulig på noen.

