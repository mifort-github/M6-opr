"""
definiraj funkcijo za izračun ploščine pravokotnega trikotnika
podani sta kateti a in b

klic funkcije naj se izvede N-krat podatke vneseš preko tipkovnice
funckiji mora biti ime trik

izpisani v oblik a =, b =, P =
"""

def trik(a, b):
    return a * b / 2

for x in range(10):
    kateta_a = float(input("vnesi kateto a: "))
    kateta_b = float(input("vnesi kateto b: "))

    P = trik(kateta_a, kateta_b)
    print("a =", kateta_a, "b = ", kateta_b, "P =", P)