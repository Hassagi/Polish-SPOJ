import sys
 
try:
	suma = 0
	for line in sys.stdin:
		n = list(map(int,line.split()))
		pom = sum(n)
		suma = suma + pom
		print(pom)
	print(suma)
except:
    sys.exit(0) 
