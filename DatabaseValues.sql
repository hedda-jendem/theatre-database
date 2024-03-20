
-- Setter opp Teater Salene 
INSERT INTO TeaterSal (SalID, Navn, Kapasitet) VALUES 
(1, 'Hovedscenen', 516),
(2, 'Gamle scene', 332),
(3, 'Studioscenen', 150),
(4, 'Teaterkjelleren', 60),
(5, 'Teaterkafeen', 100);

--Setter opp Stykkene
INSERT INTO Stykke (StykkeID, Navn, TeaterSal) VALUES 
(1, 'Kongsemnene', 1),
(2, 'Størst av alt er kjærligheten', 2);

-- Setter opp Kongsemnene Forestillinger
INSERT INTO Forestilling (Dato, Stykke) VALUES 
('2024-02-01', 1),
('2024-02-02', 1),
('2024-02-03', 1),
('2024-02-05', 1),
('2024-02-06', 1);

-- Setter opp Størst av alt er kjærligheten Forestillinger
INSERT INTO Forestilling (Dato, Stykke) VALUES 
('2024-02-03', 2),
('2024-02-06', 2),
('2024-02-07', 2),
('2024-02-12', 2),
('2024-02-13', 2),
('2024-02-14', 2);

-- Setter opp Prisliste for Kognsemnene 
INSERT INTO Prisliste (Type, Pris, Stykke) VALUES 
('Voksen', 450.00, 1),
('Honnør', 380.00, 1),
('Student', 280.00, 1),
('Gruppe 10', 420.00, 1),
('Gruppe honnør 10', 360.00, 1);

-- Setter opp Prisliste for Størst av alt er kjærligheten
INSERT INTO Prisliste (Type, Pris, Stykke) VALUES 
('Ordinær', 350.00, 2),
('Honnør', 300.00, 2),
('Barn/student', 220.00, 2),
('Grupper Over 10', 320.00, 2),
('Teaterkort Ung-medlem', 130.00, 2);


-- Skuespillere for Kongsemnene fra Trøndelag Teater
INSERT INTO Skuespiller (SkuespillerID, Navn) VALUES 
(1, 'Arturo Scotti'),
(2, 'Ingunn Beate Strige Øyen'),
(3, 'Hans Petter Nilsen'),
(4, 'Madeleine Brandtzæg Nilsen'),
(5, 'Synnøve Fossum Eriksen'),
(6, 'Emma Caroline Deichmann'),
(7, 'Thomas Jensen Takyi'),
(8, 'Per Bogstad Gulliksen'),
(9, 'Isak Holmen Sørensen'),
(10, 'Fabian Heidelberg Lunde'),
(11, 'Emil Olafsson'),
(12, 'Snorre Ryen Tøndel');

--  Roller for Kongsemnene fra Trøndelag Teater
INSERT INTO Rolle (RolleID, Navn) VALUES 
(1, 'Haakon Haakonssønn'),
(2, 'Inga fra Varteig'),
(3, 'Skule Jarl'),
(4, 'Fru Ragnhild'),
(5, 'Margrete'),
(6, 'Sigrid'),
(7, 'Ingebjørg'),
(8, 'Biskop Nikolas'),
(9, 'Gregorius Jonssonn'),
(10, 'Paal Flida'),
(11, 'Trønder 1'),
(12, 'Baard Bratte'),
(13, 'Trønder 2'),
(14, 'Jatgeir Skald'),
(15, 'Dagfinn Bonde'),
(16, 'Peter');

-- Skuespillere for Størst av alt er kjærligheten fra Trøndelag Teater
INSERT INTO Skuespiller (SkuespillerID, Navn) VALUES 
(13, 'Sunniva Du Mond Nordal'),
(14, 'Jo Saberniak'),
(15, 'Marte M. Steinholt'),
(16, 'Tor Ivar Hagen'),
(17, 'Trond-Ove Skrødal'),
(18, 'Natalie Grøndahl Tangen'),
(19, 'Åsmund Flaten');

-- Roller for Størst av alt er kjærligheten, med rollenavn som skuespillernes navn
INSERT INTO Rolle (RolleID, Navn) VALUES 
(20, 'Sunniva Du Mond Nordal'),
(21, 'Jo Saberniak'),
(22, 'Marte M. Steinholt'),
(23, 'Tor Ivar Hagen'),
(24, 'Trond-Ove Skrødal'),
(25, 'Natalie Grøndahl Tangen'),
(26, 'Åsmund Flaten');

-- RolleBesetning for Kongsemnene
INSERT INTO RolleBesetning (Skuespiller, Rolle, StykkeID) VALUES 
(1, 1, 1),  -- Arturo Scotti som Haakon Haakonssønn
(2, 2, 1),  -- Ingunn Beate Strige Øyen som Inga fra Varteig
(3, 3, 1),  -- Hans Petter Nilsen som Skule Jarl
(4, 4, 1),  -- Madeleine Brandtzæg Nilsen som Fru Ragnhild
(5, 5, 1),  -- Synnøve Fossum Eriksen som Margrete
(6, 6, 1),  -- Emma Caroline Deichmann som Sigrid
(6, 7, 1),  -- Emma Caroline Deichmann som Ingebjørg (Emma spiller både Sigrid og Ingebjørg)
(7, 8, 1),  -- Thomas Jensen Takyi som Biskop Nikolas
(8, 9, 1),  -- Per Bogstad Gulliksen som Gregorius Jonssonn
(9, 10, 1), -- Isak Holmen Sørensen som Paal Flida
(9, 11, 1), -- Isak Holmen Sørensen som Trønder 1 (Isak spiller både Paal Flida og Trønder 1)
(10, 12, 1),-- Fabian Heidelberg Lunde som Baard Bratte
(10, 13, 1),-- Fabian Heidelberg Lunde som Trønder 2 (Fabian spiller både Baard Bratte og Trønder 2)
(11, 14, 1),-- Emil Olafsson som Jatgeir Skald
(11, 15, 1),-- Emil Olafsson som Dagfinn Bonde (Emil spiller både Jatgeir Skald og Dagfinn Bonde)
(12, 16, 1);-- Snorre Ryen Tøndel som Peter


-- RolleBesetning for Størst av alt er kjærligheten
INSERT INTO RolleBesetning (Skuespiller, Rolle, StykkeID) VALUES 
(13, 20, 2), -- Sunniva Du Mond Nordal spiller seg selv
(14, 21, 2), -- Jo Saberniak spiller seg selv
(15, 22, 2), -- Marte M. Steinholt spiller seg selv
(16, 23, 2), -- Tor Ivar Hagen spiller seg selv
(17, 24, 2), -- Trond-Ove Skrødal spiller seg selv
(18, 25, 2), -- Natalie Grøndahl Tangen spiller seg selv
(19, 26, 2); -- Åsmund Flaten spiller seg selv

-- Legger til akter for Kongsemnene
INSERT INTO Akt (AktNr, Navn, Stykke) VALUES 
(1, 'Akt 1', 1),
(2, 'Akt 2', 1),
(3, 'Akt 3', 1),
(4, 'Akt 4', 1),
(5, 'Akt 5', 1);

-- Legger til akter for Størst av alt er kjærligheten
INSERT INTO Akt (AktNr, Navn, Stykke) VALUES 
(1, 'Akt 1', 2);

-- Aktene for Håkon Håkonsson i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(1, 4, 1),
(1, 5, 1);

-- Aktene for Dagfinn Bonde i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(15, 1, 1),
(15, 2, 1),
(15, 3, 1),
(15, 4, 1),
(15, 5, 1);

-- Aktene for Jatgeir Skald i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(14, 4, 1);

-- Aktene for Sigrid i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(6, 1, 1),
(6, 2, 1),
(6, 5, 1);

-- Aktene for Ingebjørg i Kongsemnene (korrigert fra 'Ingeborg')
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(7, 4, 1);

-- Aktene for Skule Jarl i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(3, 1, 1),
(3, 2, 1),
(3, 3, 1),
(3, 4, 1),
(3, 5, 1);

-- Aktene for Inga fra Varteig i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(2, 4, 1);

-- Aktene for Paal Flida i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(10, 1, 1),
(10, 2, 1),
(10, 3, 1),
(10, 4, 1),
(10, 5, 1);

-- Aktene for Fru Ragnhild i Kongsemnene 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(4, 1, 1),
(4, 5, 1);

-- Aktene for Gregorius Jonsson i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(9, 1, 1),
(9, 2, 1),
(9, 3, 1),
(9, 4, 1),
(9, 5, 1);

-- Aktene for Margrete i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(5, 1, 1),
(5, 2, 1),
(5, 3, 1),
(5, 4, 1),
(5, 5, 1);

-- Aktene for Biskop Nikolas i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(8, 1, 1),
(8, 2, 1),
(8, 3, 1);

-- Aktene for Peter i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES 
(16, 3, 1),
(16, 4, 1),
(16, 5, 1);

-- Aktene for Sunniva Du Mond Nordal i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(20, 1, 2);

-- Aktene for Jo Saberniak i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(21, 1, 2);

-- Aktene for Marte M. Steinholt i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(22, 1, 2);

-- Aktene for Tor Ivar Hagen i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(23, 1, 2);

-- Aktene for Trond-Ove Skrødal i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(24, 1, 2);

-- Aktene for Natalie Grøndahl Tangen i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(25, 1, 2);

-- Aktene for Åsmund Flaten i Størst av alt er kjærligheten 
INSERT INTO RolleIAkt (Rolle, Akt, StykkeID) VALUES
(26, 1, 2);




-- Legger til personer i Person-tabellen som jobber ved Kongsemnene
INSERT INTO Person (PersonID, Navn, Epost, AnsattStatus) VALUES 
(1, 'Yury Butusov', null, true),
(2, 'Mina Rype Stokke', null, true),
(3, 'Aleksandr Shishkin-Hokusai', null, true),
(4, 'Eivind Myren', null, true);

-- Legger til oppgaver i Oppgave-tabellen, anta at OppgaveNr er autoinkrementert, og vi bruker derfor ikke den i INSERT-setningen
INSERT INTO Oppgave (OppgaveNr, Titel, Beskrivelse, Stykke, PersonID) VALUES 
(1, 'Regi og musikkutvelgelse', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Yury Butusov')),
(2, 'Dramaturg', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Mina Rype Stokke')),
(3, 'Scenografi og kostymer', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Aleksandr Shishkin-Hokusai')),
(4, 'Lysdesign', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Eivind Myren'));

-- Legger til personer i Person-tabellen som jobber ved Størst av alt er kjærligheten
INSERT INTO Person (PersonID, Navn, Epost, AnsattStatus) VALUES 
(5, 'Jonas Corell Petersen', null, true),
(6, 'Magnus Mikaelsen', null, true),
(7, 'David Gehrt', null, true),
(8, 'Gaute Tønder', null, true),
(9, 'Kristoffer Spender', null, true);

-- Legger til oppgaver i Oppgave-tabellen
INSERT INTO Oppgave (OppgaveNr, Titel, Beskrivelse, Stykke, PersonID) VALUES 
(5, 'Regi', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Jonas Corell Petersen')),
(6, 'Lysdesign', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Magnus Mikaelsen')),
(7, 'Scenografi og kostymer', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'David Gehrt')),
(8, 'Musikalsk ansvarlig', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Gaute Tønder')),
(9, 'Dramaturg', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Kristoffer Spender'));

-- Legger til Standard kunder som bruker i brukstilfell 2 og 3 
INSERT INTO Kunde (KundeID, Navn) VALUES 
(1, 'Standarbruker'),
(2, 'Sensorbruker');

-- 
INSERT INTO Ordre (OrdreID, Kunde) VALUES 
(1, 1),
(2, 1);




