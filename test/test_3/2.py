x = int(input("Vnesi celo število: "))
while (x!=0):
    if(x%2!=0): # Če je ostanek pri deljenju z 2 enak 01 (ni nič)
        print (f'Število {x} je liho')
    else:
        print("Število",x," je sodo")
    x= int(input("Vnesi celo število: ")) # vnos novega števila x = int ( input ( " Vnesi celo število : " ) ) Da v while zanki lahko preveimo pogoj , mora bit vrednost števila x znana ' 
