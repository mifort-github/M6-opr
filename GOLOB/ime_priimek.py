"""
uporabnik vnese ime in priimek.
program izpiše ime in priimek ločeno
"""

oboje = input("vnesi ime in priimek -->")

for x, i in zip(oboje, range(len(oboje))):
    if x == " ":
        priimek = oboje[i + 1:]
        ime = oboje[:i]
        break

print("ime je:", ime, "priimek:", priimek)