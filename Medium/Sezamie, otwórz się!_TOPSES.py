import sys
 
try:
    liczba = int(input())
 
    for i in range(0, liczba):
 
        tekst1 = str(input())
        tekst2 = str(input())
 
        dlugosc1 = len(tekst1)
 
        ans = "no"
 
        for i in range(1, dlugosc1 + 1):
            if (tekst1 == tekst2):
                ans = "yes"
            tekst1 = tekst1[-1] + tekst1[:-1]
 
        print(ans)
except:
    sys.exit(0) 
