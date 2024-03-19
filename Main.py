from brukstilfelle_2 import read_hovedscene, read_gamlescenen
from brukstilfelle_4 import sjekkForestillingPaaDato
from brukstilfelle_6 import finnMestSolgteForestilling
from brukstilfelle_7 import finnSkuespillerISammeAkt
import sqlite3

def main():
    print("Hei! Velkommen til TrøndelagTeater")


    while True: 
        print("-------------------------------------------------------------")
        print("Brukstilfelle 1 er fullført og databasen er satt opp")
        print("Hvilke brukstilfellene ønsker du å kjøre?")
        print("2. Oppdatere hvilke stoler som er solgt")
        print("3. Kjøp 9 voksenbilletter til Størst av alt er kjæringheten, 3. februar")
        print("4. List opp hvilke forestillinger, og salg etter bestemt dato")
        print("5. Finne navn på skuespillere og hvilke roller og sykker de er med i")
        print("6. Finner hvilke forestillinger som er solgt best, skriver de i synkende rekkefølge")
        print("7. Finner hvilke andre skuespillere som har spilt i samme akt som gitt skuespiller")
        print("8. Avslutter programmet")
        print("-------------------------------------------------------------")

        valg = input("Skriv inn tallet til brukertilfellene du vil teste:  ")

        if valg == "2": 

            con = sqlite3.connect("TeaterDatabase.db")
            cursor = con.cursor()

            cursor.execute('INSERT INTO Kunde (KundeID, Navn) VALUES (?,?)', (1, "Standarbruker"))
            cursor.execute('INSERT INTO Ordre (OrdreID, KundeID) VALUES (?,?)', (1, 1))

            con.commit()
            con.close()

            read_hovedscene("hovedscenen.txt")
            read_gamlescenen("gamle-scene.txt")

        # elif valg == "3": 
        #     #kjører brukertilfelle_3.py
        elif valg == "4":
            dato = input("Skriv inn en dato for å se hvilke forestillinger som går og antall billetter som er solgt:  ")
            sjekkForestillingPaaDato(dato)
        # elif valg == "5":
        #     #kjører brukertilfelle_5.sql
        elif valg == "6":
            finnMestSolgteForestilling()
        elif valg == "7":
            skuespiller = input("Skriv inn navnet på en skuespiller for å finne andre skuespillere hvor de har spilt i samme akt:  ")
            finnSkuespillerISammeAkt(skuespiller)
        elif valg == "8":
            break
        else: 
            break
            
main()
