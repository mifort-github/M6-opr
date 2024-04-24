# a
def PIPravTri(a, b):
    P = a * b / 2
    return P

# b # naloga samo zahteva vnos a in b
def beri():
    a = float(input("a = "))
    b = float(input("b = "))
    return a, b

# c
a = b = 0
for i in range(5):
    a, b = beri()  # lahko le vnos a in b
    P = PIPravTri(a, b)
    print(f'{i+1}. P = {P}')