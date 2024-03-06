import random

N: list = [random.randint(1, 100) for num in range(100)]

z: int = int(input("vnesi stevilo: "))

y: int = len([num for num in N if num == z])

if y == 0:
    print(f"ni števila {z}")
else:
    print(f"število {z} se pojavi {y} krat")
