import sys
 
try:
    ilosc_testow = int(input())
    for i in range(0, ilosc_testow):
 
        wejscie = [int(i) for i in input().split()]
        ilosc = wejscie[0]
        tablica = wejscie[1:ilosc+1]
 
        srednia = sum(tablica)/ilosc
        wynik = min(tablica, key=lambda x: abs(x-srednia))
 
        print(wynik)
except:
    sys.exit(0) 
