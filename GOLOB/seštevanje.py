# seštej vse števke v nizu

niz: str = input("vnesi besedilo: ")

i: int = 0

for x in niz:
    try:
        i += int(x)
    except ValueError:
        i += 0

print(i)
