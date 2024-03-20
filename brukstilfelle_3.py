import sqlite3

def kjop_billetter(BillettType, antallBilletter, ForestillingDato, StykkeNavn, KundeID):   
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()
    
    # Finner StykkeID basert på navnet på stykket
    cursor.execute("SELECT StykkeID FROM Stykke WHERE Navn = ?", (StykkeNavn,))
    StykkeID = cursor.fetchone()[0]

    # Finner pris for billettType
    cursor.execute("SELECT Pris FROM Prisliste WHERE Type = ? AND Stykke = ?", (BillettType, StykkeID))
    Pris = cursor.fetchone()[0]

    # Setter inn ny ordre og henter OrdreID
    OrdreID = hent_neste_id("Ordre", "OrdreID", con)
    cursor.execute('INSERT INTO Ordre (OrdreID, KundeID) VALUES (?,?)', (OrdreID, KundeID)) 

    # Henter liste over ledige stoler
    ledigeStoler = ledige_stoler(cursor, ForestillingDato, StykkeID)

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
            BillettID = hent_neste_id("Billett", "BillettID", con)
            cursor.execute('INSERT INTO Billett (BillettID, OrdreID, StykkeID, Pris, BillettType, Stolnummer, Stolrad, Stolomrade, SalID, ForestillingDato) VALUES (?,?,?,?,?,?,?,?,?,?)', 
                           (BillettID, OrdreID, StykkeID, Pris, BillettType, stol[0], stol[1], stol[2], 2, ForestillingDato))
            cursor.execute('INSERT INTO Reservert (Stolnummer, Stolrad, Stolomrade, Sal, Billett, Ordre, ForestillingDato, Stykke, Kunde) VALUES (?,?,?,?,?,?,?,?,?)', 
                           (stol[0], stol[1], stol[2], 2, BillettID, OrdreID, ForestillingDato, StykkeID, KundeID))
    else:
        print("Ikke nok ledige stoler tilgjengelig.")

    con.commit()
    con.close()

    print(stolerRad)


def ledige_stoler(cursor, ForestillingDato, StykkeID):
    cursor.execute("""
        SELECT Stolnummer, Radnummer, Omradenavn
        FROM Stol 
        WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE StykkeID = ?) 
        AND (Stolnummer, Radnummer, Omradenavn) NOT IN 
        (SELECT Stolnummer, Stolrad, Stolomrade 
        FROM Billett 
        WHERE ForestillingDato = ?)""",
        (StykkeID, ForestillingDato))
    return cursor.fetchall()

# def ledige_stoler(ForestillingDato, StykkeID):
#     con = sqlite3.connect("TeaterDatabase.db")
#     cursor = con.cursor()

#     cursor.execute('''
#         SELECT Stolnummer, Radnummer, Omradenavn
#         FROM Stol 
#         WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE StykkeID = ?) 
#         AND (Stolnummer, Radnummer, Omradenavn) NOT IN 
#         (SELECT Stolnummer, Stolrad, Stolomrade 
#         FROM Billett 
#         WHERE ForestillingDato = ?)''',
#         (StykkeID, ForestillingDato))
    
#     resultater = cursor.fetchall()
#     con.commit()
#     con.close()

#     return resultater



# def hentBilletID():
#     con = sqlite3.connect("TeaterDatabase.db")
#     cursor = con.cursor()

#     cursor.execute('''
#             SELECT MAX(BillettID)
#             FROM Billett;
#             ''')

#     resultater = cursor.fetchall()

#     con.commit()
#     con.close()

#     return resultater[0][0] +1
    

def hent_neste_id(tabell, kolonne, con):
    cursor = con.cursor()
    cursor.execute(f"SELECT MAX({kolonne})+1 FROM {tabell}")
    maks_id = cursor.fetchone()[0]
    return maks_id if maks_id is not None else 1

# ledige_rad()
#ledige_stoler()


con = sqlite3.connect("TeaterDatabase.db")
cursor = con.cursor()

cursor.execute('INSERT INTO Kunde (KundeID, Navn) VALUES (?,?)', (2, "Sensorbruker"))

con.commit()
con.close()

kjop_billetter('Ordinær', 9, '2024-02-03', 'Størst av alt er kjærligheten', 2)
#kjop_billetter('Voksen', 9, '2024-02-03', 2, 2)    



  


