liczba = int(input())
tablica = []
 
for i in range(0, liczba):
    pesel = str(input())
    tablica.append(pesel)
 
for i in tablica:
    if(str(
        int(i[0])*1 + 
        int(i[1])*3 + 
        int(i[2])*7 + 
        int(i[3])*9 + 
        int(i[4])*1 + 
        int(i[5])*3 + 
        int(i[6])*7 + 
        int(i[7])*9 + 
        int(i[8])*1 + 
        int(i[9])*3 + 
        int(i[10])*1)[-1] == "0"):
        print("D")
    else:
        print("N") 
