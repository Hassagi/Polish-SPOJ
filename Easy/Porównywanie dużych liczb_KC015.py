import sys
 
while(True):
    try:
        wejscie = input()
 
        znaki = ['==', '!=', '<=', '>=']
        znak = ''
 
        for i in znaki:
            if(i in wejscie):
                znak = znak + i
 
        pom = wejscie.replace(znak, ' ')
        pom = pom.split()
        a, b = int(pom[0]), int(pom[1])
 
        if (znak == '=='):
            if(a==b): print(1)
            else: print(0)
        if (znak == '!='):
            if(a!=b): print(1)
            else: print(0)
        if (znak == '<='):
            if(a<=b): print(1)
            else: print(0)
        if (znak == '>='):
            if(a>=b): print(1)
            else: print(0)
    except:
        sys.exit(0) 
