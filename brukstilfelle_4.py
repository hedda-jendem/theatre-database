import sqlite3

def sjekkForestillingPaaDato(dato):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute("""SELECT Stykke.Navn, COUNT(Billett.BillettID) AS SolgteBilletter
                   From Forestilling
                   JOIN Stykke on Forestilling.Stykke = Stykke.StykkeID
                   LEFT JOIN Billett on Forestilling.Dato = Billett.ForestillingDato AND Forestilling.Stykke = Billett.StykkeID
                   Where Forestilling.Dato = ?
                   GROUP BY Forestilling.Dato, Stykke.Navn""", (dato,))

    rader = cursor.fetchall()
    print("Forestillinger på dato ", dato)
    print(rader)
    con.close()

# sjekkForestillingPaaDato('2024-02-03')