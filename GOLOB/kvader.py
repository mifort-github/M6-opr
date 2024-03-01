"""
program prebere podatke o kvadru: a, b, c (decimalna)
izračunaj P, V, telesna diagonala
"""

# preberemo podatke

a = float(input("število a --> "))
b = float(input("število b --> "))
c = float(input("število c --> "))

# izračunamo površino

P = 2 * (a * b + c * a + b * c)

# izračunamo volumen

V = a * b * c

# izračunamo telesno diagonalo

f = a ** 2 + b ** 2
f = f ** 0.5

t = f ** 2 + c ** 2
t = t ** 0.5

print("V = ", V)
print("P = ", P)
print("t = ", t)