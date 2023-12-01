import sys
 
try:
    wejscie = input().split()
    wejscie = [int(i) for i in wejscie]
 
    print(wejscie[0]*wejscie[1] + wejscie[2]*wejscie[3])
 
except:
    sys.exit(0) 
