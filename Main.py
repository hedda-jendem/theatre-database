from brukstilfelle_2 import read_hovedscene, read_gamlescenen
from brukstilfelle_4 import sjekkForestillingPaaDato
from brukstilfelle_5 import finnNavn
from brukstilfelle_6 import finnMestSolgteForestilling
from brukstilfelle_7 import finnSkuespillerISammeAkt
import sqlite3

def main():
    print("Hei! Velkommen til TrøndelagTeater")
    print("Hvis du har fulgt README vil brukstilfelle 1 er fullført og databasen er satt opp")


    while True: 
        print("-------------------------------------------------------------")
        print("Hvilke brukstilfeller ønsker du å kjøre?")
        print("2. Oppdatere hvilke stoler som er solgt")
        print("3. Kjøp 9 voksenbilletter til Størst av alt er kjæringheten, 3. februar")
        print("4. List opp hvilke forestillinger, og salg etter bestemt dato")
        print("5. Finne navn på skuespillere og hvilke roller og sykker de er med i")
        print("6. Finner hvilke forestillinger som er solgt best, skriver de i synkende rekkefølge")
        print("7. Finner hvilke andre skuespillere som har spilt i samme akt som gitt skuespiller")
        print("Trykk hvilken som helst annen knapp for å avslutte programmet")
        print("-------------------------------------------------------------")

        valg = input("Skriv inn tallet til brukertilfellet du vil teste:  ")

        if valg == "2": 
            read_hovedscene("hovedscenen.txt")
            read_gamlescenen("gamle-scene.txt")
        # elif valg == "3": 
        #     #kjører brukertilfelle_3.py
        elif valg == "4":
            dato = input("Skriv inn en dato for å se hvilke forestillinger som går og antall billetter som er solgt:  ")
            sjekkForestillingPaaDato(dato)
        elif valg == "5":
            finnNavn()
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
