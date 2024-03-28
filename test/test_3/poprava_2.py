"""
while: podatek ki ga preverjamo moramo pre zanko prebrati ali določiti vrednost
"""

x: float = float(input("vnesi x: "))

while x != 0:
    if x % 2 == 0:
        print("število je sodo")
    else:
        print("število je liho")

    x: float = float(input("vnesi x: "))
