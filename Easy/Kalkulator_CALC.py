def dodawanie(a, b):
    return a+b
def odejmowanie(a, b):
    return a-b
def mnożenie(a, b):
    return a*b
def dzielenie(a, b):
    return a/b
def reszta_z_dzielenia(a, b):
    return a%b
wynik = 0
while True:
    try:
        scan = str(input())
    except EOFError:
        exit(0)
    wynik = 0
    i = scan.split(' ')
    if i[0] == "+":
        wynik = dodawanie(int(i[1]), int(i[2]))
    elif i[0] == "-":
        wynik = odejmowanie(int(i[1]), int(i[2]))
    elif i[0] == "*":
        wynik = mnożenie(int(i[1]), int(i[2]))
    elif i[0] == "/":
        wynik = dzielenie(int(i[1]), int(i[2]))
    elif i[0] == "%":
        wynik = reszta_z_dzielenia(int(i[1]), int(i[2]))
    print (int(wynik)) 
