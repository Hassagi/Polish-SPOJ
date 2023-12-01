liczba = int(input())

for i in range(0, liczba):
    pretkosc_1, pretkosc_2 = map(int, input().split())
    czas_1 = 1/pretkosc_1
    czas_2 = 1/pretkosc_2
    pretkosc_srednia = int(round(2/(czas_1+czas_2), 2))
    print(pretkosc_srednia) 
