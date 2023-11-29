def czy_pierwsza(n):
    if (n == 2 or n == 3): return "TAK"
    if (n < 2 or n%2 == 0): return "NIE"
    for i in range(3, int(n**0.5) + 1, 2):
        if (n%i == 0):
            return "NIE"
    return "TAK"
 
 
ilosc = int(input())
lista = []
 
for i in range(0, ilosc):
    lista.append(int(input()))
 
for i in range(0, ilosc):
    print(czy_pierwsza(lista[i]))
