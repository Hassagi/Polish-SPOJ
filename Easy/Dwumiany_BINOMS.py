import sys
 
def silnia(n):
    pom = 1
    for i in range(1,n+1):
        pom = pom * i
    return pom
 
def symbol_newtona(n, k):
    wynik = 1
    if (n==k) or (k==0):
        return 1
    for i in range(0, k):
        wynik = wynik * (n-i)
    return int(wynik/silnia(k))
    
try:
    liczba = int(input())
    tablica = []
 
    for i in range(0, liczba):
        pom1, pom2 = map(int, input().split())
        if (pom1==pom2):
            print(1)
        else:
            print(symbol_newtona(pom1, pom2))
except:
    sys.exit(0) 
