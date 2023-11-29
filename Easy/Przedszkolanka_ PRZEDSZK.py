def NWD(a,b):
    if a == 0:
        return b
    return NWD(b % a, a)
 
def NWW(a,b):
    return (a / NWD(a,b))* b
 
liczba = int(input())
 
for i in range(0, liczba):
    x, y = map(int, input().split())
    print(int(NWW(x,y))) 
