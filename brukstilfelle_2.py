import sqlite3

#Lage dette til en funksjon?
con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

cursor.execute('INSERT INTO Kunde (KundeID, Navn) VALUES (?,?)', (1, "Standarbruker"))
cursor.execute('INSERT INTO Ordre (OrdreID, KundeID) VALUES (?,?)', (1, 1))

con.commit()
con.close()

#Størst av alt er kjærligheten spilles i gamlescenen
def read_gamlescenen(fil):

    SalID = 2
    StykkeID = 2
    Radnummer = None
    omradeNavn = None

    Omrader = {'Galleri':3, 'Balkong':4, 'Parkett':10}
    teller = 0

    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    with open(fil, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip() # for å få vekk \n

        if "Dato" in line:
            words = line.split()
            for word in words:
                if len(word) == 10 and word[4] == "-" and word[7] == "-":
                    dato = word
                    print(dato)  # print the date
        
        elif line in Omrader.keys():
            omradeNavn = line
            Radnummer = Omrader[line]
            print(omradeNavn)

        elif line.isdigit():
            for Stolnummer, char in enumerate(line.strip(), start=1):  # start=1 for å få stolnummeret til å starte på 1
                if char == '1':
                    #cursor.execute('INSERT INTO Billett (Stolnummer, Radnummer, Omradenavn, SalID, OrdreID) VALUES (?,?,?,?,?)', (Stolnummer, Radnummer, omradeNavn, SalID, 1))
                    cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', (teller, 1, StykkeID, 450, 'Voksen', Stolnummer, Radnummer, omradeNavn.strip(), SalID, dato))
                    cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', (Stolnummer, Radnummer, omradeNavn.strip(), SalID, teller, 1, dato, StykkeID, 1))
                    teller += 1
        
                    print(f"Sete {Stolnummer} i rad {Radnummer} i området {omradeNavn} er tatt med {teller}")
            Radnummer -= 1

    con.commit()
    con.close()       

 

read_gamlescenen('gamle-scene.txt')

#Oppgaven vil vel at dette skal gjøres for begge salene, både gamle scene og hovedscenen? 
#Fungerer denne funksjonen kun til gamle scene? Skulle vi ha laget den slik at det fungerer for begge salene?
#Eller skal vi ha to ulike funksjoner? 