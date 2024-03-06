import random

seznam = []

for i in range(100):
    seznam.append(random.randint(0, 100))
print(seznam)

st = int(input("Vnesi število za iskanje"))

if st in seznam:
    print("Število",st,"je v seznamu")
else:
    print("Števila",st,"ni")


st_st = 0
for x in seznam:
    if x == st:
        st_st += 1
print(st,"je",st_st,"krat v seznamu")