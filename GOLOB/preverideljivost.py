"""
preveri če je prebrano število deljivo s 3 ali 5

preveri če je prebrano število deljivo s 3 in 5
"""

x = int(input("vnesi celo število --> "))

if x % 3 == 0 or x % 5 == 0:
    print(x, "je deljivo z 3 ali 5")
else:
    print("ni")

if x % 3 == 0 and x % 5 == 0:
    print(x, "je deljivo z 3 in 5")
else:
    print("ni")
    





