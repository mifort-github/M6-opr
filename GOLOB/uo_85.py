"""
funkcija z imenom "vrni_samoglasnike" iz danega niza izpise samoglasnike v istem vrstnem redu
"""

niz: str = "Hello World!"


def vrni_samoglasnike(niz: str) -> str:

    novo: str = ""

    for x in niz:
        if x in "AEIOUaeiou":
            novo += x

    return novo


def vrni_soglasnike(niz: str) -> str:

    novo: str = ""

    for x in niz:
        if x not in "AEIOUaeiou":
            novo += x

    return novo


print(vrni_samoglasnike(niz))
print(vrni_soglasnike(niz))
