from brukstilfelle_2 import read_hovedscene, read_gamlescenen
from brukstilfelle_4 import sjekkForestillingPaaDato
from brukstilfelle_5 import finnNavn
from brukstilfelle_6 import finnMestSolgteForestilling
from brukstilfelle_7 import finnSkuespillerISammeAkt
from brukstilfelle_3 import kjop_billetter
import sqlite3

def main():
    print("")
    print("Hei! Velkommen til Trøndelag Teater!")
    print("")
    print("Hvis du har fulgt instruksjonene i README vil brukstilfelle 1 allerede være fullført, og databasen er satt opp")
    print("")


    while True: 
        print("-------------------------------------------------------------")
        print("Hvilke brukstilfeller ønsker du å kjøre?")
        print("2. Oppdatere hvilke stoler som er solgt")
        print("3. Kjøp 9 voksenbilletter til Størst av alt er kjærligheten, 3. februar")
        print("4. List opp hvilke forestillinger, og antall salg etter bestemt dato")
        print("5. Finn navn på skuespillere og hvilke roller og stykker de er med i")
        print("6. Finn hvilke forestillinger som har solgt best, skrevet ut i synkende rekkefølge")
        print("7. Finn hvilke andre skuespillere som har spilt i samme akt som angitt skuespiller")
        print("Trykk hvilken som helst annen knapp for å avslutte programmet")
        print("-------------------------------------------------------------")

        valg = input("Skriv inn tallet til brukertilfellet du vil teste:  ")

        if valg == "2": 
            read_hovedscene("hovedscenen.txt")
            read_gamlescenen("gamle-scene.txt")
        elif valg == "3": 
            kjop_billetter('Ordinær', 9, '2024-02-03', 2, 2) 
        elif valg == "4":
            dato = input("Skriv inn en dato for å se hvilke forestillinger som går og antall billetter som er solgt:  ")
            sjekkForestillingPaaDato(dato)
        elif valg == "5":
            finnNavn()
        elif valg == "6":
            finnMestSolgteForestilling()
        elif valg == "7":
            skuespiller = input("Skriv inn navnet på en skuespiller for å se hvilke skuespilllere de har spilt med i samme akt:  ")
            finnSkuespillerISammeAkt(skuespiller)
        elif valg == "8":
            break
        else: 
            break
            
main()
