import sys
 
try:
    while(True):
        tekst = input()
        pom = [str(i) for i in tekst]
        pom.reverse()
        for i in pom:
            print(i, end = '')
        print()
except:
    sys.exit(0) 
