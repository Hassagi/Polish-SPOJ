def czy_palindrom(n):
    pom1 = [int(x) for a, x in enumerate(str(n))]
    pom2 = pom1.copy()
    pom2.reverse()
    if (pom1 == pom2):
        return True
    else: 
        return False
 
def dodawanie(n):
    pom1 = [str(x) for a, x in enumerate(str(n))]
    pom1.reverse()
    pom1 = "".join(pom1)
    return int(pom1)+n
 
liczba = int(input())
 
for i in range(0, liczba):
    temp = int(input())
    suma = 0
    while(True):
        if (czy_palindrom(temp)==True):
            print(temp, suma)
            break
        else:
            suma = suma + 1
            temp = dodawanie(temp) 
