"""
s for prepiši besedičlo iz prvega niza v drugi niz
NizNov=NizStari
"""
NizStar = input("shaizen")


def NarediTole():
    NizNov = " "

    for i in range(1):
        NizNov = NizStar[::-1]

    print(NizNov, NizStar)


NarediTole()