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
    Stykke int not null,
    primary key (Dato, Stykke),
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
    StykkeID int not null
    primary key (Akt, Rolle),
    foreign key (Rolle) references Rolle(RolleID)
    on update cascade
    on delete cascade,
    foreign key (Akt, StykkeID) references Akt(AktNr, StykkeID)
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
    Mobilnummer varchar(20),
    Navn varchar(30) not null,
    Adresse text 
);

-- Oppretter Ordre tabellen
create table Ordre (
    OrdreID int primary key,
    Dato date,
    Tid time,
    KundeID int not null,
    TotalPris decimal(6, 2),
    Antall int,
    foreign key (KundeID) references Kunde(KundeID)
);

--Oppretter Billett tabellen
create table Billett (
    BillettID int,
    OrdreID int not null,
    StykkeID int not null,
    Pris int not null,
    BillettType varchar(30) not null,
    Stolnummer int not null,
    Stolrad int not null,
    Stolomrade varchar(30) not null,
    SalID int not null,
    ForestillingDato date not null,
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
    foreign key (Stolnummer, Stolrad, Stolomrade) references Stol(Stolnummer, Radnummer, Omradenavn)
        on update cascade
        on delete cascade
    foreign key (SalID) references TeaterSal(SalID)
        on update cascade
        on delete cascade
    foreign key (ForestillingDato) references Forestilling(Dato)
        on update cascade
        on delete cascade
);

--Oppretter Reservert tabellen
CREATE TABLE Reservert (
    Stolnummer INT NOT NULL,
    Stolrad INT NOT NULL,
    Stolomrade VARCHAR(30) NOT NULL,
    Sal INT NOT NULL,
    Billett INT NOT NULL,
    Ordre INT NOT NULL,
    ForestillingDato DATE NOT NULL,
    Stykke INT NOT NULL,
    Kunde INT NOT NULL,
    PRIMARY KEY (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde),
    FOREIGN KEY (Stolnummer, Stolrad, Stolomrade, Sal) REFERENCES Stol(Stolnummer, Radnummer, Omradenavn, SalID)
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    FOREIGN KEY (Billett,Ordre) REFERENCES Billett(BillettID,OrdreID)
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    FOREIGN KEY (ForestillingDato,Stykke) REFERENCES Forestilling(Dato,StykkeID)
        ON UPDATE CASCADE 
        ON DELETE CASCADE,
    FOREIGN KEY (Kunde) REFERENCES Kunde(KundeID)
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

