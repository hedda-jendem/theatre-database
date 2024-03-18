import sqlite3


def finnNavn(fil):
    con = sqlite3.connect("TeaterDatabase.db")

    cursor = con.cursor()
    cursor.execute('''SELECT Stykke.Navn AS Teaterstykke, Skuespiller.Navn AS Skuespiller, Rolle.Navn AS Rolle
               FROM Stykke
               JOIN RolleBesetning ON Stykke.StykkeID = RolleBesetning.Stykke
               JOIN Skuespiller ON RolleBesetning.Skuespiller = Skuespiller.SkuespillerID
               JOIN Rolle ON RolleBesetning.Rolle = Rolle.RolleID''')
    

    resultater = cursor.fetchall

    for rad in resultater:
        print(f'Teaterstykke: {rad[0]}, Skuespiller: {rad[1]}, Rolle: {rad[2]}')

    con.close()