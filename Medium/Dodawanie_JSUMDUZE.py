import sys
 
try:
	liczba = int(input())
	for i in range(0, liczba):
		wejscie = input().split()
		wejscie = [int(i) for i in wejscie]
		print(sum(wejscie))
except:
	sys.exit(0) 
