import sys
 
def letter_to_number(character):
    number = ord(character) - 96
    return number
 
try:
    szachownica1 = [[0]*8 for i in range(8)]
    szachownica2 = [[0]*8 for i in range(8)]
 
    wejscie = [int(i) for i in input().split()]
    a, b = wejscie[0], wejscie[1]
 
    gracz = []
    przeciwnik = []
 
    for i in range(0, a):
        wiersz = input().split()
        figura = str(wiersz[0])
        pozycja = str(wiersz[1])
        gracz.append((figura, pozycja))
        y, x = int(letter_to_number(pozycja[0]))-1, int(pozycja[1])-1
        szachownica1[x][y]=figura
 
    for i in range(0, b):
        wiersz = input().split()
        figura = str(wiersz[0])
        pozycja = str(wiersz[1])
        przeciwnik.append((figura, pozycja))
        y, x = int(letter_to_number(pozycja[0]))-1, int(pozycja[1])-1
        szachownica2[x][y]=figura
 
    pom1 = sorted(przeciwnik, key=lambda element: (element[0], element[1]))
    pom2 = sorted(gracz, key=lambda element: (element[0], element[1]))
 
    for i in range(7, -1, -1):
        print(*szachownica2[i], sep='')
    for i in pom1:
        print(*i)
    print()
    for i in range(7, -1, -1):
        print(*szachownica1[i], sep='')
    for i in pom2:
        print(*i)
except:
    sys.exit(0) 
