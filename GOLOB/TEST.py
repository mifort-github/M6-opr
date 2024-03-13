from random import randint

a: int = int(input("vnesi število a: "))
b: int = int(input("vnesi število b: "))

N: list = [randint(a, b) for x in range(2000)]

print(N)
