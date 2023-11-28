liczba = int(input())
for i in range(0, liczba):
    inp = input()
    inputs = inp.split()
    inputs.pop(0)
    inputs.reverse()
    inputs = [int(i) for i in inputs]
    
    for j in inputs:
        print(j, end=" ")
    print() 
