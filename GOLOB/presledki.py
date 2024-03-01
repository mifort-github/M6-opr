"""
preštej koliko presliedkov vsebuje stavek.
"jutri se bom poboljšal"
"""

stavek = "jutri se bom poboljšal"

presledki = 0

print("število presledkov je:", stavek.count(" ")) # not good

for x in stavek:
    if x == " ":
        presledki += 1

print("število presledkov je:", presledki)

presledki = 0
a = 0

while a < len(stavek):
    if stavek[a] == " ":
        presledki += 1
    a += 1

print("število presledkov je:", presledki)