"""
s for zanko prepiši besedilo iz prvega niza v drugega
"""

niz1: str = "ghiagffauilgfauč.ghoagfiual"


def prepis(niz):
    niz2: str = ""

    for x in niz1:
        niz2 = niz2 + x

    return niz2


print(niz1)
print(prepis(niz1))
