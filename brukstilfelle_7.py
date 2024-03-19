import sqlite3

def finnSkuespillerISammeAkt(skuespiller):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    resultat = []

    #SQL spørring som finner alle aktene den skuespilleren er med i
    cursor.execute("""SELECT Akt FROM RolleIAkt WHERE Rolle IN 
                   (SELECT Rolle FROM Skuespiller WHERE Navn = ?)""",(skuespiller))
    listeMedAkter = cursor.fetchall()
    
    #SQL spørring som finner alle skuespillere som er med i de samme aktene 
    for akt in listeMedAkter:
        cursor.execute("""SELECT DISTINCT Skuespiller.Navn FROM Skuepiller 
                       JOIN RolleIAkt ON Skuespiller.SkuespillerID = RolleIAkt.Rolle
                       WHERE RolleIAkt = ?""", (akt))
    listeOverSkuespillereIAktene = cursor.fetchall()

    print(listeMedAkter)
    print(listeOverSkuespillereIAktene)
    con.close()



    #Håkon Håkonsson
    #Arturo Scotti