import sys
 
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]
 
try:
    while(True):
        wymiar = int(input())
    
        tablica = []
        wejscie1 = input().split()
        wejscie1 = [int(j) for j in wejscie1]
        wejscie2 = input().split()
        wejscie2 = [int(j) for j in wejscie2]
        macierz1 = to_matrix(wejscie1, wymiar)
        macierz2 = to_matrix(wejscie2, wymiar)
    
        for i in range(0, wymiar):
            for j in range(0, wymiar):
                pom = sum([a*b for a,b in zip(macierz1[i],list(zip(*macierz2))[j])])
                tablica.append(pom)
 
        for i in tablica:
            print(i, end=' ')
        print()
 
except:
    sys.exit(0) 
