import math
import sys
 
slownik = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}
 
def convert(liczba, podstawa):
    tekst = ""
    while(liczba != 0):
        reszta = liczba % podstawa
        liczba = math.floor(liczba/podstawa)
        if reszta in slownik.keys():
            tekst += str(slownik[reszta])
        else:
            tekst += str(reszta)
    return tekst[::-1]
 
try:
    liczba_testow = int(input())
    for i in range(0, liczba_testow):
        liczba = int(input())
        print(convert(liczba, 16), convert(liczba, 11))
except:
    sys.exit(0) 
