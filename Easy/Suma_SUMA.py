suma = 0
 
while True:
    try:
        liczba = int(input())
    except EOFError:
        exit(0)
    suma += liczba
    print(suma) 
