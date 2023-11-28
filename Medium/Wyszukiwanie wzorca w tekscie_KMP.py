import sys
 
try:
    liczba = int(input())
    for i in range(0, liczba):
        pom = input()
        substring = str(input())
        string = str(input())
 
        for num in [i for i in range(len(string)) if string.startswith(substring, i)]:
            print(num)
except:
    sys.exit(0) 
