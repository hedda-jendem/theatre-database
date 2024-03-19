import sqlite3

def kjop_billetter():   

    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()
    
    # Finner StykkeID for "Størst av alt er kjærligheten"
    cursor.execute("SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten'")
    StykkeID = cursor.fetchone()[0]
    ForestillingDato = '2024-02-03'
    BillettType = 'Voksen'
    cursor.execute("SELECT Pris FROM Billett WHERE BillettType = 'Voksen'")
    Pris = cursor.fetchone()[0]

    # Setter inn ny kunde og henter KundeID
    cursor.execute('INSERT INTO Kunde (KundeID, Navn) VALUES (?,?)', (None, "Sensorbruker"))
    KundeNr = cursor.lastrowid

    # Setter inn ny ordre
    cursor.execute('INSERT INTO Ordre (OrdreID, KundeID) VALUES (?,?)', (None, KundeNr)) 

    ledigRad = ledige_rad()
    antallLedigeStoler = ledigRad[3]

    antall_kjopte = 0
    Stoler = []

    for i in range(1, antallLedigeStoler+1):
        if antall_kjopte == 9:
            break
        if (i, ledigRad[0], ledigRad[1]) not in cursor.execute('SELECT Stolnummer, Stolrad, Stolomrade FROM Billett WHERE ForestillingDato = ?', (ForestillingDato,)).fetchall():
            print(f"Sete {i} i rad {ledigRad[0]} i området {ledigRad[1]} er tatt")

            Stol = (i, ledigRad[0], ledigRad[1], StykkeID, Pris, BillettType)
            Stoler.append(Stol)
            
            cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', (i+50, 2, StykkeID, Pris, BillettType, i, ledigRad[0], ledigRad[1], 2, ForestillingDato))
            cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', (i, ledigRad[0], ledigRad[1], 2, i+50, 2, ForestillingDato, StykkeID, 2))
            antall_kjopte += 1

    con.commit()
    con.close()

    print(f"Du har kjøpt {antall_kjopte} billetter til forestillingen Størst av alt er kjærligheten den 3. februar 2024")
    print(f"Du har kjøpt setene {Stoler}")


def ledige_rad(): 
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute('''
            SELECT Radnummer, Omradenavn, SalID, COUNT(*)
            FROM Stol 
            WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten') 
            AND (Stolnummer, Radnummer, Omradenavn) NOT IN 
            (SELECT Stolnummer, Stolrad, Stolomrade 
            FROM Billett 
            WHERE ForestillingDato = '2024-02-03') 
            GROUP BY Radnummer, Omradenavn, SalID 
            ORDER BY Omradenavn;
            ''')

    resultater = cursor.fetchall()
    print(resultater[0])

    con.commit()
    con.close()

    return resultater[0] #Velger ut den første raden med 9 ledige stoler


def ledige_stoler():
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute('''
            SELECT Stolnummer, Radnummer, Omradenavn
            FROM Stol 
            WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten') 
            AND (Stolnummer, Radnummer, Omradenavn) NOT IN 
            (SELECT Stolnummer, Stolrad, Stolomrade 
            FROM Billett 
            WHERE ForestillingDato = '2024-02-03');
            ''')

    resultater = cursor.fetchall()

    con.commit()
    con.close()


ledige_rad()
ledige_stoler()
kjop_billetter()    



  


