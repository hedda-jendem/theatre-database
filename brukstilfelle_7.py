import sqlite3

def finnSkuespillerISammeAkt(skuespiller):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    resultat = []

    #SQL spørring som finner alle aktene en skuespiller er med i
    cursor.execute("""SELECT Akt, StykkeID FROM RolleIAkt 
                   WHERE Rolle = (SELECT Rolle FROM RolleBesetning 
                   WHERE Skuespiller = (SELECT SkuespillerID FROM Skuespiller 
                   WHERE Navn = ?))""", (skuespiller,))
    listeMedAkter = cursor.fetchall()

    #SQL spørring som finner alle skuespillere som er med i de samme aktene 
    for akt in listeMedAkter:
        AktNr = akt[0]
        SkuespillID = akt[1]
        cursor.execute("""SELECT DISTINCT Skuespiller.Navn, Stykke.Navn FROM RolleIAkt 
                       JOIN Skuespiller ON RolleIAkt.Rolle = Skuespiller.SkuespillerID
                       JOIN Stykke ON RolleIAkt.StykkeID = Stykke.StykkeID
                       WHERE RolleIAkt.Akt = ? AND Skuespiller.Navn != ? AND RolleIAkt.StykkeID = ?
                       """, (AktNr, skuespiller, SkuespillID,))
        listeOverSkuespillereMedIAkt = cursor.fetchall()
        resultat.append(listeOverSkuespillereMedIAkt)

    con.close()

    print("")
    print(f'Her kommer alle skuespillere som har spilt med {skuespiller}, og hvilket skuespill det skjedde i')
    for lineEN in resultat:
        for lineTO in lineEN:
            print(f'{skuespiller} spilte med {lineTO[0]} i {lineTO[1]}')


    #Arturo Scotti