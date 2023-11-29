import math
 
R, D = map(float, input().split())
 
r = math.sqrt (R**2 - ((1/2)*D)**2 )
pole = math.pi * r**2
 
print(pole) 
