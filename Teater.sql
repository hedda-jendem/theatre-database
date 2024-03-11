-- Oppretter TeaterSal tabellen
create table TeaterSal (
    SalID int primary key,
    Navn varchar(30) not null,
    Kapasitet int not null
);

-- Oppretter Stol tabellen
create table Stol (
    Stolnummer int not null,
    Radnummer int not null,
    Omradenavn varchar(30) not null,
    SalID int not null,
    primary key (Stolnummer, Radnummer, Omradenavn, SalID),
    foreign key (SalID) references TeaterSal(SalID)
    on update no action
    on delete no action
);

-- Oppretter Forestilling tabellen
create table Forestilling (
    Dato date not null,
    Klokkeslett time not null,
    Stykke int not null,
    primary key (Dato, Klokkeslett, Stykke),
    foreign key (Stykke) references Stykke(StykkeID)
    on update cascade
    on delete no action
);

-- Oppretter Stykke tabellen
create table Stykke (
    StykkeID int primary key,
    Navn varchar(30) not null,
    TeaterSal int,
    foreign key (TeaterSal) references TeaterSal(SalID)
    on update cascade
    on delete no action
);

-- Oppretter Akt tabellen
create table Akt (
    AktNr int primary key,
    Navn varchar(30) not null,
    Stykke int not null,
    foreign key (Stykke) references Stykke(StykkeID)
    on update no action
    on delete cascade --hvis et stykke slettes vil alle tilknyttede Akt-rader også bli slettet
);

-- Oppretter Rolle tabellen
create table Rolle (
    RolleID int primary key,
    Navn varchar(30) not null
);

-- Oppretter RolleIAkt tabellen
create table RolleIAkt (
    Akt int not null,
    Rolle int not null,
    primary key (Akt, Rolle),
    foreign key (Rolle) references Rolle(RolleID)
    on update cascade
    on delete cascade,
    foreign key (Akt) references Akt(AktNr)
    on update cascade
    on delete cascade 
);

-- Oppretter Skuespiller tabellen
create table Skuespiller (
    SkuespillerID int primary key,
    Navn varchar(30) not null
);

-- Oppretter RolleBesetning tabellen
create table RolleBesetning (
    Skuespiller int not null,
    Rolle int not null,
    primary key (Skuespiller, Rolle),
    foreign key (Skuespiller) references Skuespiller(SkuespillerID)
    on update no action
    on delete no action,
    foreign key (Rolle) references Rolle(RolleID)
    on update no action
    on delete no action
);

-- Oppretter Prisliste tabellen
create table Prisliste (
    Type varchar(30) not null,
    Pris decimal(6, 2) not null,
    Stykke int not null,
    primary key (Type, Stykke),
    foreign key (Stykke) references Stykke(StykkeID)
    on update no action 
    on delete cascade
);

-- Oppretter Person tabellen
create table Person (
    PersonID int primary key,
    Navn varchar(30) not null,
    Epost varchar(30),
    AnsattStatus boolean
);

-- Oppretter Oppgave tabellen
create table Oppgave (
    OppgaveNr int primary key,
    Titel varchar(30) not null,
    Beskrivelse text,
    Stykke int not null,
    PersonID int not null,
    foreign key (Stykke) references Stykke(StykkeID)
    on update cascade
    on delete no action, --sletting av stykke går ikke hvis det er oppgaver avhegig av det 
    foreign key (PersonID) references Person(PersonID)
    on update cascade
    on delete no action
);

-- Oppretter Kunde tabellen
create table Kunde (
    KundeID int primary key,
    Mobilnummer varchar(20) not null,
    Navn varchar(30) not null,
    Adresse text not null
);

-- Oppretter Ordre tabellen
create table Ordre (
    OrdreID int primary key,
    Dato date not null,
    Tid time not null,
    KundeID int not null,
    TotalPris decimal(6, 2) not null,
    Antall int not null,
    foreign key (KundeID) references Kunde(KundeID)
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
