"""
preberi celi števili M in N 
izpiši rezultan celoštevilskega deljenja in ostanek pri deljenju
v obliki "7/2 je 3, ost. 1"
"""

M = int(input("vpiši M --> ")) # branje M
N = int(input("vpiši N --> ")) # branje N
CeliDel = M // N
Ostanek = M % N 
Decimalka = M / N

print(str(M) + "//" + str(N) + " = " + str(CeliDel)) # + pomeni združi nize
print(str(M) + "%" + str(N) + " = " + str(Ostanek)) # , izpiše števila kot števila
print(str(M) + "/" + str(N) + " = " + str(Decimalka)) # + združevanje nizov str(število)
print