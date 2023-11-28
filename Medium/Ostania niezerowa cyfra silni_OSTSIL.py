import sys
 
sys.setrecursionlimit(1500)
 
def funkcja_pomocnicza(n, wynik, suma_piatek):
    liczba = n
    if liczba == 1:
        return
 
    while (liczba % 5 == 0):
        liczba = int(liczba / 5)
        suma_piatek = suma_piatek + 1
 
    while (suma_piatek != 0 and (liczba & 1) == 0):
        liczba >>= 1
        suma_piatek = suma_piatek - 1
 
    wynik[0] = (wynik[0] * (liczba % 10)) % 10
    funkcja_pomocnicza(n - 1, wynik, suma_piatek)
 
def ostatnia_niezerowa_cyfra_silni(n):
    if(n==0):
        return 1
 
    wynik = [1]
    funkcja_pomocnicza(n, wynik, 0)
    return wynik[0]
 
 
try:
    liczba_testow = int(input())
 
    for i in range(0, liczba_testow):
        pom = int(input())
        print(int(ostatnia_niezerowa_cyfra_silni(pom)))
except EOFError:
    sys.exit(0)
