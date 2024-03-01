"""
opisne ocene
1 = nezadostno
2 = zadostno
3 = dobro
4 = prav dobro
5 = odlično
"""

ocena = int(input("ocena -->")) #le zaporedne if stavke

if ocena == 1:
    print("nezadostno")
else:
    if ocena == 2:
        print("zadostno")
    else:
        if ocena == 3:
            print("dobro")
        else:
            if ocena == 4:
                print("prav dobro")
            else:
                if ocena == 5:
                    print("odlično")
                else:
                    print("neveljavna ocena")


