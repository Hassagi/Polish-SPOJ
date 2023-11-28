import string
import sys
 
slownik = {}
 
try:
 
    while(True):
        try:
            wejscie = str(input()).split(" ")
            imie = wejscie[2].upper()
            if imie in slownik:
                slownik.update({imie:slownik[imie]+1})
            else:
                slownik.update({imie:1})
        except:
            break
    
    pom = sorted(slownik.items(), key=lambda x:(-x[1],x[0]))
    for i in pom:
        print(*i)
 
except:
    sys.exit(0) 
