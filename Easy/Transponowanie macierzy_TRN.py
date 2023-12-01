def podzial_tablicy(tablica, n):
    for i in range(0, len(tablica), n):
        yield tablica[i:i + n]
 
n, m = input().split()
n = int(n)
m = int(m)
 
tablica = []
for i in range(0, n):
        pom = input()
        tablica.append(pom.split())
 
tablica2 = []
pom = 0
 
for j in range(0,m):
    for i in tablica:
        tablica2.append(i[pom])
    pom = pom + 1
 
tablica2 = [int(i) for i in tablica2]
 
macierz = list(podzial_tablicy(tablica2, n))
 
for wiersz in macierz:
    for liczba in wiersz:
        print(liczba, end=" ")
    print() 
