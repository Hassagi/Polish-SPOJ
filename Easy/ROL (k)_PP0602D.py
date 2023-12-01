wejscie = input().split()
wejscie = [int(i) for i in wejscie]
 
liczby = input().split()
liczby = [int(i) for i in liczby]
 
n = wejscie[0]
k = wejscie[1]
 
liczby = liczby[0:n]
liczby = liczby[k:] + liczby[:k]
 
for i in liczby:
    print(i, end = " ") 
