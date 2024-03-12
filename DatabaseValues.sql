
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
INSERT INTO Forestilling (Dato, Klokkeslett, Stykke) VALUES 
('2024-02-01', '19:00', 1),
('2024-02-02', '19:00', 1),
('2024-02-03', '19:00', 1),
('2024-02-05', '19:00', 1),
('2024-02-06', '19:00', 1);

-- Setter opp Størst av alt er kjærligheten Forestillinger
INSERT INTO Forestilling (Dato, Klokkeslett, Stykke) VALUES 
('2024-02-03', '18:30', 2),
('2024-02-06', '18:30', 2),
('2024-02-07', '18:30', 2),
('2024-02-12', '18:30', 2),
('2024-02-13', '18:30', 2),
('2024-02-14', '18:30', 2);

-- Setter opp Prisliste for Kognsemnene 
INSERT INTO Prisliste (Type, Pris, Stykke) VALUES 
('Voksen', 450.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Kongsemnene')),
('Honnør', 380.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Kongsemnene')),
('Student', 280.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Kongsemnene')),
('Gruppe 10', 420.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Kongsemnene')),
('Gruppe honnør 10', 360.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Kongsemnene'));

-- Setter opp Prisliste for Størst av alt er kjærligheten
INSERT INTO Prisliste (Type, Pris, Stykke) VALUES 
('Ordinær', 350.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten')),
('Honnør', 300.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten')),
('Barn/student', 220.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten')),
('Grupper Over 10', 320.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten')),
('Teaterkort Ung-medlem', 130.00, (SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten'));

-- Skuespillere for Størst av alt er kjærligheten fra Trøndelag Teater
INSERT INTO Skuespiller (SkuespillerID, Navn) VALUES 
(8, 'Sunniva Du Mond Nordal'),
(9, 'Jo Saberniak'),
(10, 'Marte M. Steinholt'),
(11, 'Tor Ivar Hagen'),
(12, 'Trond-Ove Skrødal'),
(13, 'Natalie Grøndahl Tangen'),
(14, 'Åsmund Flaten');

-- Roller for Størst av alt er kjærligheten, med rollenavn som skuespillernes navn
INSERT INTO Rolle (RolleID, Navn) VALUES 
(13, 'Sunniva Du Mond Nordal'),
(14, 'Jo Saberniak'),
(15, 'Marte M. Steinholt'),
(16, 'Tor Ivar Hagen'),
(17, 'Trond-Ove Skrødal'),
(18, 'Natalie Grøndahl Tangen'),
(19, 'Åsmund Flaten');

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
(1, 'Haakon Haakonssnn'),
(2, 'Inga fra Varteig'),
(3, 'Skule Jarl'),
(4, 'Fru Ragnhild'),
(5, 'Margrete (Skules datter)'),
(6, 'Sigrid (Skules søster) / Ingebjørg'),
(7, 'Biskop Nikolas'),
(8, 'Gregorius Jonssonn'),
(9, 'Paal Flida / Trønder'),
(10, 'Baard Bratte / Trønder'),
(11, 'Jatgeir Skald / Dagfinn Bonde'),
(12, 'Peter (prest og Ingebjørgs sønn)');

-- RolleBesetning for Kongsemnene
INSERT INTO RolleBesetning (Skuespiller, Rolle) VALUES 
(1, 1),  -- Arturo Scotti som Haakon Haakonssnn
(2, 2),  -- Ingunn Beate Strige Øyen som Inga fra Varteig (Haakons mor)
(3, 3),  -- Hans Petter Nilsen som Skule Jarl
(4, 4),  -- Madeleine Brandtzæg Nilsen som Fru Ragnhild (Skules hustru)
(5, 5),  -- Synnøve Fossum Eriksen som Margrete (Skules datter)
(6, 6),  -- Emma Caroline Deichmann som Sigrid (Skules søster) / Ingebjørg
(7, 7),  -- Thomas Jensen Takyi som Biskop Nikolas
(8, 8),  -- Per Bogstad Gulliksen som Gregorius Jonssonn
(9, 9),  -- Isak Holmen Sørensen som Paal Flida / Trønder
(10, 10), -- Fabian Heidelberg Lunde som Baard Bratte / Trønder
(11, 11), -- Emil Olafsson som Jatgeir Skald / Dagfinn Bonde
(12, 12); -- Snorre Ryen Tøndel som Peter (prest og Ingebjørgs sønn)

-- RolleBesetning for Størst av alt er kjærligheten
INSERT INTO RolleBesetning (Skuespiller, Rolle) VALUES 
(8, 13),  -- Sunniva Du Mond Nordal spiller seg selv
(9, 14),  -- Jo Saberniak spiller seg selv
(10, 15), -- Marte M. Steinholt spiller seg selv
(11, 16), -- Tor Ivar Hagen spiller seg selv
(12, 17), -- Trond-Ove Skrødal spiller seg selv
(13, 18), -- Natalie Grøndahl Tangen spiller seg selv
(14, 19); -- Åsmund Flaten spiller seg selv

-- Legger til akter for Kongsemnene
INSERT INTO Akt (AktNr, Navn, Stykke) VALUES 
(1, 'Akt 1', 1),
(2, 'Akt 2', 1),
(3, 'Akt 3', 1),
(4, 'Akt 4', 1),
(5, 'Akt 5', 1);

-- Aktene for Håkon Håkonsson i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 1),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 2),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 3),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 4),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 5);

-- Aktene for Håkon Håkonsson i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 1),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 2),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 3),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 4),
((SELECT RolleID FROM Rolle WHERE Navn = 'Håkon Håkonsson'), 5);

-- Aktene for Inga fra Varteig i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Jatgeir Skald'), 4);

INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Sigrid'), 1),
((SELECT RolleID FROM Rolle WHERE Navn = 'Sigrid'), 2),
((SELECT RolleID FROM Rolle WHERE Navn = 'Sigrid'), 5);

-- Aktene for Skule Jarl i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Ingebjørg'), 4);

-- Aktene for Fru Ragnhild i Kongsemnene
INSERT INTO RolleIAkt (Rolle, Akt) VALUES 
((SELECT RolleID FROM Rolle WHERE Navn = 'Guttorm Ingesson'), 1);


-- Legger til personer i Person-tabellen som jobber ved Kongsemnene
INSERT INTO Person (PersonID, Navn, Epost, AnsattStatus) VALUES 
(next value for person_seq, 'Yury Butusov', null, true),
(next value for person_seq, 'Mina Rype Stokke', null, true),
(next value for person_seq, 'Aleksandr Shishkin-Hokusai', null, true),
(next value for person_seq, 'Eivind Myren', null, true);

-- Legger til oppgaver i Oppgave-tabellen, anta at OppgaveNr er autoinkrementert, og vi bruker derfor ikke den i INSERT-setningen
INSERT INTO Oppgave (Titel, Beskrivelse, Stykke, PersonID) VALUES 
('Regi og musikkutvelgelse', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Yury Butusov')),
('Dramaturg', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Mina Rype Stokke')),
('Scenografi og kostymer', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Aleksandr Shishkin-Hokusai')),
('Lysdesign', null, 1, (SELECT PersonID FROM Person WHERE Navn = 'Eivind Myren'));

-- Legger til personer i Person-tabellen
INSERT INTO Person (PersonID, Navn, Epost, AnsattStatus) VALUES 
(next value for person_seq, 'Jonas Corell Petersen', null, true),
(next value for person_seq, 'Magnus Mikaelsen', null, true),
(next value for person_seq, 'David Gehrt', null, true),
(next value for person_seq, 'Gaute Tønder', null, true),
(next value for person_seq, 'Kristoffer Spender', null, true);

-- Legger til oppgaver i Oppgave-tabellen
INSERT INTO Oppgave (Titel, Beskrivelse, Stykke, PersonID) VALUES 
('Regi', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Jonas Corell Petersen')),
('Lysdesign', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Magnus Mikaelsen')),
('Scenografi og kostymer', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'David Gehrt')),
('Musikalsk ansvarlig', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Gaute Tønder')),
('Dramaturg', null, 2, (SELECT PersonID FROM Person WHERE Navn = 'Kristoffer Spender'));



