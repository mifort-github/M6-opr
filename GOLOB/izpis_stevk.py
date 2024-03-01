"""
izpis števk celega števila 
a) while zanka
b) for zanka
"""

#while

st = 6304031403

while st > 0:
    print(st % 10)
    st = st // 10

print("--------------------------------------------------------------------------")
# for

st = 6304031403

for x in str(st):
    print(x)
