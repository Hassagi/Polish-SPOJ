x = -1
liczba = int(input())
 
for i in range(0, liczba):
    wejscie = input().split()
    wejscie = [int(i) for i in wejscie]
    pom = wejscie[0]
    wejscie = wejscie[1:pom+1]
    wejscie = wejscie[-x:] + wejscie[:-x]
    for i in wejscie:
        print(i, end=" ")
    print() 
