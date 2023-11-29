from math import floor, ceil
import sys
 
ilosc_testow = int(input())
 
for i in range(0, ilosc_testow):
    try:
        wejscie = input().split()
        wejscie = [int(i) for i in wejscie]
 
        liczba_obzartuchow, ilosc_w_podelku = wejscie[0], wejscie[1]
 
        suma = 0
        for i in range(0, liczba_obzartuchow):
            czas = int(input())
            suma = suma + floor(86400/czas)
 
        wynik = ceil(suma/ilosc_w_podelku)
        print(int(wynik))
    except:
        sys.exit(0) 
