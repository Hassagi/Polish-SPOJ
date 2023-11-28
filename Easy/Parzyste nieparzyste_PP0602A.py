import sys
 
def change(tab):
    array = []
    for i in range(1, len(tab), 2):
        array.append(tab[i])
    for i in range(0, len(tab), 2):
        array.append(tab[i])
    return array
 
try:
    liczba_testow = int(input())
    for i in range(0, liczba_testow):
        wejscie = [int(i) for i in input().split()]
        wejscie = wejscie[1:]
        print(*change(wejscie))
except:
    sys.exit(0) 
