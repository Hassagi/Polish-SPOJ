liczba = int(input())
tablica = []
 
for i in range(0, liczba):
    pom1, pom2 = map(int, input().split())
    tablica.append((pom1, pom2))
 
def last_digit(a, b):
    a = int(a)
    b = int(b)
 
    if (a == 0) and (b == 0):
        return 1
       
    if (b == 0):
        return 1
       
    if (a == 0):
        return 0
 
    #last_digit_in_base = int(str(a)[-1])
    if (b%4==0):
        exp = 4
    else:
        exp = b%4
    
    ldigit = pow(a, exp)
 
    return ldigit%10
 
for i in tablica:
    print(last_digit(i[0], i[1])) 
