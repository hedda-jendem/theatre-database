import sqlite3


def finnSkuespillerISammeAkt(skuespiller):
    con = sqlite3.connect("TeaterDatabase.db")
    cursor = con.cursor()

    resultat = []

    # SQL spørring som finner alle unike aktene en skuespiller er med i, uavhengig av rolle
    cursor.execute("""SELECT DISTINCT RolleIAkt.Akt, RolleIAkt.StykkeID FROM RolleIAkt 
                      JOIN RolleBesetning ON RolleIAkt.Rolle = RolleBesetning.Rolle
                      JOIN Skuespiller ON RolleBesetning.Skuespiller = Skuespiller.SkuespillerID
                      WHERE Skuespiller.Navn = ?""", (skuespiller,))
    listeMedAkter = cursor.fetchall()

    # SQL spørring som finner alle skuespillere som er med i de samme aktene
    for akt in listeMedAkter:
        AktNr = akt[0]
        SkuespillID = akt[1]
        cursor.execute("""SELECT DISTINCT Skuespiller.Navn, Stykke.Navn FROM RolleIAkt 
                          JOIN Stykke ON RolleIAkt.StykkeID = Stykke.StykkeID
						  JOIN RolleBesetning ON RolleBesetning.Rolle  = RolleIAkt.Rolle
                          JOIN Skuespiller ON RolleBesetning.Skuespiller = Skuespiller.SkuespillerID
                          WHERE RolleIAkt.Akt = ? AND Skuespiller.Navn != ? AND RolleIAkt.StykkeID = ?
                          """, (AktNr, skuespiller, SkuespillID,))
        listeOverSkuespillereMedIAkt = cursor.fetchall()
        resultat.extend(listeOverSkuespillereMedIAkt)  # Endret fra append til extend for å flate ut listen

    con.close()

    print("\nHer kommer alle skuespillere som har spilt med {}, og hvilket skuespill det skjedde i:".format(skuespiller))
    for skuespillerNavn, stykkeNavn in set(resultat):  # Bruker set for å eliminere duplikater
        print(f"{skuespiller} spilte med {skuespillerNavn} i {stykkeNavn}")
