def liczby_pierwsze(lower, upper):
    lower, upper = int(lower), int(upper)
    tab = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                tab.append(num)  
    return tab
 
def odkoduj(wejscie):
    suma = 0
    for i in liczby_pierwsze(lower, upper):
        slowo = ""
        for letter_code in wejscie:
            if((letter_code % i) >= 65 and (letter_code % i) <= 90):
                slowo = slowo + chr((letter_code % i))
            else:
                break
        if (len(slowo) == len(wejscie)):
            wynik = [int(i), " ", str(slowo), "\n"]
            suma = suma + 1
    if (suma == 1):
        return wynik
    else:
        return [str("NIECZYTELNE")]
 
lower = 120
upper = 150
 
liczba = int(input())
 
for i in range(0, liczba):
    pom = int(input())
    wejscie = input().split()
    wejscie = [int(i) for i in wejscie]
    wejscie = wejscie[0:pom]
    wynik = odkoduj(wejscie)
    for i in wynik:
        print(i, end="") 
