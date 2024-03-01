st = int(input("vnesi število: "))

for x in range(st):
    for y in range(x):
        if y == 0 or y == x-1:
            print("+", end="")
        else:
            print("-", end="")
    print()