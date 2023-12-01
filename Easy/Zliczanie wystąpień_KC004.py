while(True):
    try:
        suma = 0
 
        wejscie = input().split()
        wejscie = [int(i) for i in wejscie]
 
        liczba = wejscie[0]
        dlugosc = wejscie[1]
 
        tablica = wejscie[2:dlugosc + 2]
 
        for i in tablica:
            if (i==liczba):
                suma+=1
        print(int(suma))
    except:
        break 
