def NWD(a, b):
    while True:
        reszta = a%b
        if (reszta == 0):
            return b
        else:
            a = b
            b = reszta
 
liczba = int(input())
tablica = []
 
for i in range(0, liczba):
    pom1, pom2 = map(int, input().split())
    tablica.append(NWD(pom1, pom2))
 
for i in tablica:
    print(i) 
