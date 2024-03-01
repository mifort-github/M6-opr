starost =  int(input("vpiši starost --> "))     #vstopnice_10_10_2023 poglej v zvezek
cena = 36

if starost >= 18:
    print("plačaj -->" + str(cena))
if starost <= 5:
    print("plačaj -->" + str(cena * 0))
if starost > 5 and starost < 18:
    print("plačaj -->" + str(int(cena / 2)))