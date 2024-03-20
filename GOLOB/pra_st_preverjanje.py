N: int = 12
a: bool = True

for x in range(2, int(N ** 0.5) + 1):
    if N % x == 0:
        a = False
        break

print(a)
