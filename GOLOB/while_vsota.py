"""
while
seštevaj prebrana števila dokler je vsota manjša od 2024
prišteješ lahko le števila ki so večja od 0 in manjša od 200
"""

vsota = 0

while vsota < 2024:
    st = float(input("vnesi število večje od 0 in manjše od 200: "))
    if st > 0 and st < 200:
        vsota += st
        print("število 2024 je doseženo")
    else:
        print("število ni veljavno")