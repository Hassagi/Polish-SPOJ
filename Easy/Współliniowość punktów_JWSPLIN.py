def prosta(A, B):
    x_A, y_A = float(A[0]), float(A[1])
    x_B, y_B = float(B[0]), float(B[1])
    if ((x_A != x_B) and (y_A != y_B)):
        pom1 = 1
        pom2 = -((y_A-y_B)/(x_A-x_B))
        pom3 = -(y_A - ((y_A-y_B)/(x_A-x_B)) * x_A)
        return [float(pom1), float(pom2), float(pom3)]
    if (x_A == x_B):
        return [1, 0, -float(x_A)]
    if (y_A == y_B):
        return [0, 1, -float(y_A)]
 
liczba = int(input())
 
for i in range(0, liczba):
    wejscie = input().split()
    wejscie = [int(i) for i in wejscie]
 
    A = wejscie[0:2]
    B = wejscie[2:4]
    C = wejscie[4:6]
 
    if (A==B):
        if (A==C):
            print("TAK")
            continue
        else:
            print("NIE")
            continue
 
    if (A[0] == B[0]):
        if (A[0] == C[0]):
            print("TAK")
            continue
        else:
            print("NIE")
            continue
 
    if (A[1] == B[1]):
        if (A[1] == C[1]):
            print("TAK")
            continue
        else:
            print("NIE")
            continue
 
 
    rownanie = prosta(A, B)
    if (C[1] + rownanie[1] * C[0] + rownanie[2] == 0):
        print("TAK")
        continue
    else:
        print("NIE")
        continue 
