"""
preveri, če je število sodo ali liho

število je sodo, če je deljivo z 2... ostanek je 0
 a st % 2 == 0
"""

x = int(input("vpiši celo število "))

if x % 2 == 0:
    sodo = True
else:
    sodo = False

if sodo:
    print(str(x) + " je sodo")

else:
    print(str(x) + " je liho")