a = 11
b = 22

# normal

print("a =", a)
print("b =", b)

c = a # 11
a = b # 22
b = c

print("a =", a)
print("b =", b)

# python

a,b = b,a

print("a =", a)
print("b =", b)