liczba = int(input())
 
for i in range(0, liczba):
 
    wejscie = int(input())
    suma = 0
 
    while(wejscie != 1):
        if(wejscie%2==1):
            wejscie = 3*wejscie+1
            suma = suma + 1
        else:
            wejscie = wejscie/2
            suma = suma + 1
 
    print(int(suma)) 
