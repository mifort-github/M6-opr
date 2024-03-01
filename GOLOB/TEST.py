seznam: list = ["Jon", "Jaka", "Maks", "Nik", "Tristan", "Maks", "Žan"]

seznam_len: int = len(seznam)

for x in seznam:
    print(x, end=", ")

print()

for x in range(seznam_len - 1, -1, -1):
    print(seznam[x], end=", ")
