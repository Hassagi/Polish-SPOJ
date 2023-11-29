liczba = int(input())
wyniki = []
 
for i in range(0, liczba):
    n = int(input())
    tablica = [int(num) for num in input().split(" ", n-1)]
    wyniki.append(sum(tablica))
 
for i in wyniki:
    print(i) 
