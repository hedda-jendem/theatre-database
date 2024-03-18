import sqlite3

def checkPerformancesOnDate(dato):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute("""SELECT Stykke.Navn, COUNT(Billett.BillettID) AS SolgteBilletter 
                      FROM Stykke 
                      LEFT JOIN Forestilling ON Forestilling.Stykke = Stykke.StykkeID
                      LEFT JOIN Billett ON Billett.ForestillingDato = Forestilling.Dato 
                      WHERE Forestilling.Dato = ? 
                      GROUP BY Stykke.StykkeID;""", (dato,))
    
    rader = cursor.fetchall()
    print("Forestillinger på dato ", dato)
    print(rader)
    con.close()

# checkPerformancesOnDate('2024-02-03')