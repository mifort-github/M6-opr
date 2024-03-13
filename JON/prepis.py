"""
S for zanko prepiši besedilo iz prvega niza v drugi niz, v obratnem vrstnem redu
Marec -> ceraM
"""

# Prva
def preObr(niz): #brez for
    obrat = niz[::-1]
    return obrat


prepis1 = preObr("Peri aaca")
print("Prepis", preObr)



# Druga
def obrRev(niz):
    drugi = ""
    for crka in reversed(niz): # reversed: začne z desne
        drugi += crka
    return drugi

prepis2 = obrRev("Perica reže raci rep.")
print("obrRev", prepis2)



# Tretja
def obrniFor(niz):
    drugi = ""
    for crka in (niz[::-1]): # -1 začne zadaj
        drugi += crka
    return drugi

prepis3 = obrniFor("Milharcic")
print("obrniFor", prepis3)



# Četrta
def upRange(niz):
    drugi = ""
    for i in range(len(niz)-1,-1,-1): # začne z len..., konča z 0, korak 1 levo
        drugi += niz[i]
    return drugi

prepis4 = upRange("osama bin laden")
print("upRange:", prepis4)


#Milhracicia ber

def Milharcic(niz):
    drugi =""
    for i in range(1):
        drugi = niz[::-1]
    return drugi

prepis5 = Milharcic("Domen jebe v usta")
print("UpRange:", prepis5)