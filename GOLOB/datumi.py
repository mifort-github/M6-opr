"""datum: 03012024 spremeni v 03. 01. 2024 težje 3. 1. 2024"""

datum = "03012024"

dan = datum[:2]
mesec = datum[2:4]
leto = datum[4:8]

print(dan + ".", mesec + ".", leto)

#print(datum[1:2] + ".", datum[3:4] + ".", datum[4:8])

if dan[0] == "0":
    dan = dan[1]
if mesec[0] == "0":
    mesec = mesec[1]

print(dan + ".", mesec + ".", leto)