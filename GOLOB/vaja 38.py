"""
funkcija z imenom: zdruzi_niza
prebere 2 niza
izvedi tudi klic
"""


def zdruzi_niza(a: str, b: str) -> str:
    return a + b


str1: str = input("vnesi prvi niz: ")
str2: str = input("vnesi drugi niz: ")

print(zdruzi_niza(str1, str2))
