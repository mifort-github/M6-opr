"""
če je N enak 5 bomo napisali
*****
ooooo
ooooo
ooooo
*****
"""

N = int(input("število: "))

for x in range(N):
    if x == 0 or x == N - 1:
        for y in range(N):
            print("*", end="")
        print()
    else:
        for y in range(N):
            print("o", end="")
        print()

# vse pravice pridržane, Jaka Golob Šajn©