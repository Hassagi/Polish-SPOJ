wejscie = input().split()
tablica = [float(i) for i in wejscie]
 
a = tablica[0]
b = tablica[1] - tablica[2]
 
if(a != 0):
	print('{:.2f}'.format(round(-b/a,2)))
elif((a == 0) and (b == 0)):
	print("NWR")
else:
	print("BR")
 
