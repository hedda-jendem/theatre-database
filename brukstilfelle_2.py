import sqlite3

teller = 1

#Størst av alt er kjærligheten spilles i gamlescenen
def read_gamlescenen(fil):

    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    global teller

    SalID = 2
    StykkeID = 2
    Radnummer = None
    omradeNavn = None

    Omrader = {'Galleri':3, 'Balkong':4, 'Parkett':10}

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
        
        elif line in Omrader.keys():
            omradeNavn = line
            Radnummer = Omrader[line]
            #print(omradeNavn)

        elif line.isdigit():
            for Stolnummer, char in enumerate(line.strip(), start=1):  # start=1 for å få stolnummeret til å starte på 1
                if char == '1':
                    cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', (teller, 1, StykkeID, 450, 'Voksen', Stolnummer, Radnummer, omradeNavn.strip(), SalID, dato))
                    cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', (Stolnummer, Radnummer, omradeNavn.strip(), SalID, teller, 1, dato, StykkeID, 1))
                    teller += 1
        
                    #print(f"Sete {Stolnummer} i rad {Radnummer} i området {omradeNavn} er tatt med {teller}")
            Radnummer -= 1

    con.commit()
    con.close() 

    print("Gamlescenen er ferdig lest")     

#Kongsemnen spilles i hovedscenen
def read_hovedscene(fil):

    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    global teller
    StolnummerTeller = 525

    SalID = 1
    StykkeID = 1
    Radnummer = None
    omradeNavn = None

    Omrader = {'Parkett':18, 'Galleri':4}

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
        
        elif  "Parkett" in line:
            omradeNavn = "Parkett"
            Radnummer = 18
        elif "Galleri" in line: 
            omradeNavn = "Galleri"
            Radnummer = 1

        else:
            for char in reversed(line):

                StolnummerTeller -= 1

                if char == '1':
                    cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', (teller, 1, StykkeID, 450, 'Voksen', StolnummerTeller, Radnummer, omradeNavn.strip(), SalID, dato))
                    cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', (StolnummerTeller, Radnummer, omradeNavn.strip(), SalID, teller, 1, dato, StykkeID, 1))
                    teller += 1

                    #print(f"Sete {Stolnummer} i rad {Radnummer} i området {omradeNavn} er tatt med {teller}")
                elif char == 'x':
                    continue

        
            if omradeNavn == 'Parkett':
                Radnummer -= 1   

    con.commit()
    con.close() 

    print("Hovedscenen er ferdig lest")      
