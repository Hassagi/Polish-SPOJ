from textwrap import wrap
import sys
 
slownik1 = {
    "A":0,
    "B":1,
    "C":2,
    "D":3,
    "E":4,
    "F":5,
    "G":6,
    "H":7,
    "I":8,
    "J":9,
    "K":10,
    "L":11,
    "M":12,
    "N":13,
    "O":14,
    "P":15,
}
 
slownik2 = {
    "A":0,
    "B":16,
    "C":32,
    "D":48,
    "E":64,
    "F":80,
    "G":96,
    "H":112,
    "I":128,
    "J":144,
    "K":160,
    "L":176,
    "M":192,
    "N":208,
    "O":224,
    "P":240,
}
 
try:
 
    for wejscie in sys.stdin:
 
        tab = []
        wejscie = wrap(wejscie,2)
        
        for i in wejscie:
            tab.append(chr(slownik1[i[0]]+slownik2[i[1]]))
 
        tab = "".join(tab)
 
        print(str(tab))
except:
    sys.exit(0) 
