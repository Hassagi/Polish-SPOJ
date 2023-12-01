import sys
 
def is_number(s):
    try:
        int(s)
        return True
    except:
        return False
 
try:
    while(True):
        liczby = 0
        slowa = 0
        wejscie = list(map(str, input().split()))
        
        for i in wejscie:
            if is_number(i):
                liczby = liczby + 1
            else:
                slowa = slowa + 1
        print(liczby, slowa)
        
except:
    sys.exit(0) 
