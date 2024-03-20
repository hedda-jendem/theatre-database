import sqlite3

def finnMestSolgteForestilling():
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    cursor.execute("""SELECT Stykke.Navn, Forestilling.Dato, COUNT(Billett.BillettID) AS SolgteBilletter
                   FROM Forestilling
                   JOIN Stykke ON Forestilling.Stykke = Stykke.StykkeID 
                   LEFT JOIN Billett ON Forestilling.Dato = Billett.ForestillingDato AND Forestilling.Stykke = Billett.StykkeID
                   GROUP BY Forestilling.Dato, Stykke.Navn
                   ORDER BY SolgteBilletter DESC;""")
    
    rader = cursor.fetchall()
    print("Alle forestillinger sortert i synkende rekkefølge etter salg")
    for rad in rader:
        stykkeNavn, dato, solgteBilletter = rad
        print(f"Stykke: {stykkeNavn}, Dato: {dato}, Solgte billetter: {solgteBilletter}")
    
    con.close()