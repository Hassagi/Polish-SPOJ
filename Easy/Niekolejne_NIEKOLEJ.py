import sys
 
try:
    liczba = int(input())
    tab = []
 
    if liczba==0:
        print(0)
    if liczba <= 2:
        print("NIE")
 
    for i in range(1, liczba+1, 2):
        tab.append(i)
    for i in range(0, liczba+1, 2):
        tab.append(i)
 
    print(*tab)
except:
    sys.exit(0) 
