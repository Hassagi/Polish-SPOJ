from math import sqrt
from operator import itemgetter
import sys
 
try:
    liczba_testow = int(input())
 
    for j in range(0, liczba_testow):
        liczba = int(input())
        table = []
        for i in range(0, liczba):
            pom = input().split()
            pom[0], pom[1], pom[2] = pom[0][0:10], int(pom[1]), int(pom[2])
            pom.append( sqrt(pom[1]**2+pom[2]**2) )
            table.append(pom)
        table = sorted(table, key=itemgetter(3))
        for i in table:
            print(*i[0:3], sep=" ")
        input()
except:
    sys.exit(0) 
