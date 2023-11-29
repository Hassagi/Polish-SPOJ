import sys
 
try:
    while(True):
        wejscie = input().split()
        wejscie = [float(n) for n in wejscie]
        a, b, c = wejscie[0], wejscie[1], wejscie[2]
        delta = b**2 - 4*a*c
        if (delta > 0):
            print(2)
        elif(delta == 0):
            print(1)
        else:
            print(0)
except:
    sys.exit() 
