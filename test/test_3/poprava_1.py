"""
funkcija z imenom PIPrav, podatka: a, b
"""


def piprav(x: float, y: float) -> float:
    p = a * b / 2
    return p


a: float = float(input("vnesi a: "))
b: float = float(input("vnesi b: "))

for x in range(27):
    print(piprav(a, b))
