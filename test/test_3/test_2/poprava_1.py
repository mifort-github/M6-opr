import math


def Pitagora(a, b):
    return math.sqrt(a ** 2 + b ** 2)


a = float(input("a = "))
b = float(input("b = "))

for x in range(27):
    c = Pitagora(a, b)
    print("Dolžina hipotenuze je", c)
