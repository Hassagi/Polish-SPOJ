liczba = int(input())
for i in range(0, liczba):
    tekst = str(input())
    polowa = int(len(tekst)/2)
    pom = tekst[0:polowa]
    print(pom)
