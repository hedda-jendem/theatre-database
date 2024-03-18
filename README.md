# Dokumentasjon

## Hvordan bruke databasen:

1. Sørg for at du er i mappen databaser-db2.
2. Kjør filen `SetUpDatabase.py`. Dette vil sette opp databasen med all nødvendig informasjon.
3. Kjør filen `Main.py`. Dette vil starte programmet.
4. Følg deretter instruksjonene i terminalen.

**Merk:**

- Alle datoer for forestillinger må skrives på formen yyyy-mm-dd
- Du kan ikke starte med å skrive mellomrom i terminalen når du velger hvilke deler av programmet du vil kjøre

## Endringer i databasen gjort etter DB1:

-**Klokkeslett**: Dropper klokkeslett i databasen siden alle forestillinger som viser samme stykke starter samtidig.

-**Organisering av billettabeller**: Vi fjerner tabellene BillettType og BillettForestilling, til fordel for en enkel Billett-tabell. Tidligere var begge tabellene, BillettType og BillettForestilling, på 4. NF. Etter nærmere arbeid med databasen har vi innsett at det er mindre fordelaktig å ha to tabeller på 4. NF, fremfor én tabell som gjør databasen enklere å bruke.

--Oppretter Billett tabellen
create table Billett (
BillettID int primary key,
OrdreID int not null,
StykkeID int not null,
Pris int not null,
Stolnummer int not null,
Stolrad int not null,
Stolomrade varchar(30) not null,
SalID int not null,
primary key (OrdreID, BillettID),
foreign key (OrdreID) references Ordre(OrdreID)
on update cascade
on delete cascade
foreign key (StykkeID) references Stykke(StykkeID)
on update cascade
on delete cascade
foreign key (Pris) references Prisliste(Pris)
on update cascade
on delete cascade
foreign key (Stolnummer, Stolrad, Stolomrade) references Stol(Stolnummer, Stolrad, Stolomrade)
on update cascade
on delete cascade
foreign key (SalID) references TeaterSal(SalID)
on update cascade
on delete cascade
);

-- Oppretter BillettType tabellen
create table BillettType (
BillettID int not null,
OrdreID int not null,
Type varchar(30) not null,
primary key (OrdreID, BillettID),
foreign key (OrdreID) references Ordre(OrdreID)
on update cascade
on delete cascade,
foreign key (Type) references Prisliste(Type)
on update cascade
on delete cascade
);

-- Oppretter BillettForestilling tabellen
create table BillettForestilling (
OrdreID int not null primary key,
StykkeID int not null,
foreign key (OrdreID) references Ordre(OrdreID)
on update cascade
on delete no action,
foreign key (StykkeID) references Stykke(StykkeID)
on update cascade
on delete no action
);

-- Oppretter ResevertForestilling tabellen
create table ReservertForestilling (
OrdreID int not null,
ForestillingDato date not null,
ForestillingKl time not null,
Stykke int not null,
primary key (OrdreID),
foreign key (OrdreID) references BillettForestilling(OrdreID)
on update cascade
on delete cascade,
foreign key (ForestillingDato, ForestillingKl) references Forestilling(Dato, Klokkeslett)
on update cascade
on delete cascade,
foreign key (Stykke) references Stykke(StykkeID)
on update no action
on delete cascade
);

-- Oppretter ReservertStol tabellen
create table ReservertStol (
BillettID int not null,
OrdreID int not null,
Stolnummer int not null,
Radnummer int not null,
Omradenavn varchar(30) not null,
SalID int not null,
primary key (OrdreID, BillettID),
foreign key (BillettID,OrdreID) references BillettType(BillettID,OrdreID)
on update cascade
on delete cascade,
foreign key (Stolnummer, Radnummer, Omradenavn, SalID) references Stol(Stolnummer, Radnummer, Omradenavn, SalID)
on update cascade
on delete cascade,
foreign key (OrdreID) references Ordre(OrdreID)
on update cascade
on delete cascade
);
