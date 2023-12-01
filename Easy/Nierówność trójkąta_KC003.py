import sys
 
def check(tab):
    for i in tab:
        if(i<=0):
            return False
    return True
 
 
try:
    while(True):
        wejscie = input().split()
        wejscie = [float(i) for i in wejscie]
        
        if (check(wejscie) == False):
            print(0)
            continue
            
        wejscie.sort()
        if (wejscie[0] + wejscie[1] > wejscie[2]):
            print(1)
            continue
        else:
            print(0)
            continue
except:
    sys.exit(0) 
