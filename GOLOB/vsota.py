"""
sešteva prebrana cela števila, manjša od 23, toliko časa, dokler je vsota manjša 2023
"""

vsota = 0 

while vsota < 2023:
    a = int(input("vnesi število manjše od 23 -->"))
    if a < 23:
        vsota += a
    else:
        print("napaka poskrbi, da je število manjše od 23")
