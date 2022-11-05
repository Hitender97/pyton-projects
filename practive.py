phrase="My Academy"
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[4])
print(phrase.index("d"))
print(phrase.replace("My","Cloud"))
print(2 * 7 + 4)
print(2 * (7 + 4))
A=45
B=(str(A)) #this will be helpful when we need to print the int with string.
print(type(B))
print(pow(2,2))
B=-10
print(abs(B)) #absolute value
print(max(4, 6))
print(min(6, 4))
A=5.453
print(round(A)) # we can use floor function from math module

from math import *
print(floor(A))
print(ceil(A)) # ceil will always return higer number
print(sqrt(36))