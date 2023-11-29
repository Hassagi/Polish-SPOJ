def silnia(n):
    if (n >= 10):
        return 0
 
    fac = 1
     
    for i in range(1, n + 1):
        fac = (fac * i) % 100
 
    return fac
 
 
liczba = int(input())
tablica = []
 
for i in range(0,liczba):
    n = int(input())
    tablica.append(n)
 
for i in range(0, len(tablica)):
    temp = str(silnia(tablica[i]))
    if (len(temp) < 2):
        print(0, temp[0])
    else:
        print(temp[0], temp[1]) 
