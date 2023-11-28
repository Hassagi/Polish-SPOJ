import sys
 
try:
    wejscie = [int(i) for i in input().split()]
    x1, y1, x2, y2, x3, y3 = wejscie[0], wejscie[1], wejscie[2], wejscie[3], wejscie[4], wejscie[5]
    S1 = 0.5 * ((x2 * x2 * y3 + y2 * y2 * y3 - x1 * x1 * y3 + x1 * x1 * y2 - y1 * y1 * y3 + y1 * y1 * y2 + y1 * x3 * x3 + y1 * y3 * y3 - y1 * x2 * x2 - y1 * y2 * y2 - y2 * x3 * x3 - y2 * y3 * y3) / (y1 * x3 - y1 * x2 - y2 * x3 - y3 * x1 + y3 * x2 + y2 * x1))
    S2 = 0.5 * ((-x1 * x3 * x3 - x1 * y3 * y3 + x1 * x2 * x2 + x1 * y2 * y2 + x2 * x3 * x3 + x2 * y3 * y3 - x2 * x2 * x3 - y2 * y2 * x3 + x1 * x1 * x3 - x1 * x1 * x2 + y1 * y1 * x3 - y1 * y1 * x2) / (y1 * x3 - y1 * x2 - y2 * x3 - y3 * x1 + y3 * x2 + y2 * x1))
    R = ((S1-x1)**2+(S2-y1)**2)**(1/2)
    print("{:.2f}".format(R))
except:
    sys.exit(0)
