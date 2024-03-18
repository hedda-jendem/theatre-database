import sqlite3

def kjop_billetter(fil):   

    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()
    
    # Finner StykkeID for "Størst av alt er kjærligheten"
    stykkeID = cursor.execute("SELECT StykkeID FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten'")
    ForestillingDato = '2024-02-03'
    BillettType = 'Voksen'

    con.commit()
    con.close()


def ledige_stoler(): 
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute("SELECT Stolrad FROM Stol WHERE Stolnummer,Stolrad, Stolomrade NOT IN (SELECT Stolnummer,Stolrad,Stolomrade, FROM Billett WHERE (ForestillingDato = ?))", (ForestillingDato))

    con.commit()
    con.close()





  


