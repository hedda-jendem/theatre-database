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

    cursor.execute("SELECT Radnummer, Omradenavn, SalID "
               "FROM Stol "
               "WHERE SalID = (SELECT TeaterSal FROM Stykke WHERE Navn = 'Størst av alt er kjærligheten') "
               "AND (Stolnummer, Radnummer, Omradenavn) NOT IN "
               "(SELECT Stolnummer, Stolrad, Stolomrade "
               "FROM Billett "
               "WHERE ForestillingDato = '2024-02-03') "
               "GROUP BY Radnummer, Omradenavn, SalID "
               "HAVING COUNT(*) > 9 "
               "ORDER BY Omradenavn;")

    con.commit()
    con.close()





  


