import sqlite3


def finnNavn():
    con = sqlite3.connect("TeaterDatabase.db")

    cursor = con.cursor()
    cursor.execute("""SELECT Stykke.Navn AS Teaterstykke, Skuespiller.Navn AS Skuespiller, Rolle.Navn AS Rolle
                FROM Stykke 
                JOIN RolleBesetning  ON Stykke.StykkeID = RolleBesetning.StykkeID
                JOIN Skuespiller ON RolleBesetning.Skuespiller = Skuespiller.SkuespillerID
                JOIN Rolle  ON RolleBesetning.Rolle = Rolle.RolleID
                GROUP BY Stykke.Navn, Skuespiller.Navn, Rolle.Navn
                ORDER BY Stykke.Navn, Skuespiller.Navn""")
    

    resultater = cursor.fetchall()
    print("-------------------------------------------------------------")
    print("Her kommer teaterstykke, navn på skuespiller og tilhørende rolle: ")
    print('')

    for rad in resultater:
       print(f'{rad[0]} - {rad[1]} - {rad[2]}')

    con.close()
