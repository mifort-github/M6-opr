"""
*oo*
*oo*
*oo*
*oo*
"""

st = int(input("vnesi stevilo: "))

for vrstice in range(st):
    print("*", end=" ")
    for stolpci in range(st-2):
        print("o", end=" ")
    print("*")