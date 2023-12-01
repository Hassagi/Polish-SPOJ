import sys
import string
 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
 
d = {}
text = ""
 
try:
    number = int(input())
    for i in range(0, number):
        text = text + str(input())
 
    for i in text:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
 
    for l in lower + upper:
        if l in d:
            print(l, d[l])
except:
    sys.exit(0) 
