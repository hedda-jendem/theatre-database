import sqlite3

def kjop_billetter(BillettType, antallBilletter, ForestillingDato, StykkeID, KundeID):   
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    # Finner pris for billettType
    cursor.execute('SELECT Pris FROM Prisliste WHERE Type = ? AND Stykke = ?', (BillettType, StykkeID))
    Pris = cursor.fetchone()[0]

    # Setter inn ny ordre og henter OrdreID
    OrdreID = hent_nesteID("Ordre", "OrdreID", con)
    cursor.execute('INSERT INTO Ordre (OrdreID, KundeID) VALUES (?,?)', (OrdreID, KundeID)) 

    # Henter liste over ledige stoler
    ledigeStoler = ledige_stoler(ForestillingDato, StykkeID)

    # Velger ledige stoler på samme rad
    stolerRad = []
    for stol in ledigeStoler:
        if len(stolerRad) == 0 or (stolerRad[-1][1] == stol[1] and stolerRad[-1][2] == stol[2]):
            stolerRad.append(stol)
        else:
            stolerRad = [stol]

        if len(stolerRad) == antallBilletter:
            break

    if len(stolerRad) == antallBilletter:
        for stol in stolerRad:
            BillettID = hent_nesteID("Billett", "BillettID", con)
            cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', 
                           (BillettID, OrdreID, StykkeID, Pris, BillettType, stol[0], stol[1], stol[2], 2, ForestillingDato))
            cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', 
                           (stol[0], stol[1], stol[2], 2, BillettID, OrdreID, ForestillingDato, StykkeID, KundeID))
    else:
        print("Ikke nok ledige stoler tilgjengelig.")

    con.commit()
    con.close()

    print(f"OrdreID: {OrdreID} - KundeID: {KundeID} - Antall billetter: {antallBilletter} - Pris: {Pris} - ForestillingDato: {ForestillingDato} - StykkeID: {StykkeID}")

def ledige_stoler(ForestillingDato, StykkeID):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute('''
        SELECT Stolnummer, Radnummer, Omradenavn
        FROM Stol 
        WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE StykkeID = ?) 
        AND (Stolnummer, Radnummer, Omradenavn) NOT IN 
        (SELECT Stolnummer, Stolrad, Stolomrade 
        FROM Billett 
        WHERE ForestillingDato = ?)''',
        (StykkeID, ForestillingDato))
    
    resultater = cursor.fetchall()
    con.commit()
    con.close()

    return resultater
    

def hent_nesteID(tabell, kolonne, con):
    cursor = con.cursor()
    cursor.execute(f"SELECT MAX({kolonne})+1 FROM {tabell}")
    maks_id = cursor.fetchone()[0]
    return maks_id if maks_id is not None else 1





  


