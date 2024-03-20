"""
1. način število N deljiš z vsemi števili med 1 in N
1 in N sta vedno deljitelja
"""


def del1(n: int) -> list:
    a: list = [deljitelj for deljitelj in range(1, n+1) if n % deljitelj == 0]

    return a


for x in del1(int(input("vnesi število: "))):
    print(x, end=" ")
