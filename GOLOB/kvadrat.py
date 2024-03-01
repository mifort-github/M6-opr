st = int(input("vnesi število: "))

for x in range(st):
    for y in range(st):
        if y != st - 1:
            print("🟥", end="")
        else:
            print("🟥")