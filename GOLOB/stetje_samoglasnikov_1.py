"""
preštej samoglasnike (male črke) v povedi
"""

besedilo = "kajghdlieiouahgwduila"

i = 0

for x in besedilo:
    if x == "a" or x == "e" or  x == "i" or x == "o" or x == "u":
        i += 1

print("samoglasnikov je", i)