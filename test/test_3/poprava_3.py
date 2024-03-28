"""
pojavnost znakov M A R E C
"""

bes: str = "danes smo marca"


def stejmarec(besedilo: str) -> int:
    i: int = 0
    for x in besedilo:
        if x in "MARECmarec":
            i += 1

    return i


print(stejmarec(bes))
