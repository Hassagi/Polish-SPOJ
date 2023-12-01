import sys
 
try:
    suma = 0
    for i in range(0, 3):
        liczba = int(input())
        suma = suma + liczba
    print(suma)
except:
    sys.exit(0)
