import datetime
import sqlite3

def checkPerformancesOnDate(dato):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute("SELECT Forestilling.Stykke, Stykke.Navn FROM Forestilling INNER JOIN Stykke ON Forestilling.Stykke = Stykke.StykkeID WHERE Forestilling.Dato = ?;", (dato,))
    
    rader = cursor.fetchall()
    print("Forestillinger på dato ", dato)
    print(rader)
    con.close()

checkPerformancesOnDate('2024-02-03')