x = float(input("vnesi število x -->"))
y = float(input("vnesi število y -->"))
z = float(input("vnesi število z -->"))

print("x je", x)
print("y je", y)
print("z je", z)

if x >= y and x >= z:
    print("x je največje")
elif y >= x and y >= z:
    print("y je največje")
elif z >= x and z >= y:
    print("z je največje")