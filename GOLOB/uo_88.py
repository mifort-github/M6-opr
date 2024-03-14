"""
preštej samoglasnike v nizu
"""

niz: str = "Hello World!"


def st_sam(niz: str) -> int:
    i: int = 0

    for x in niz:
        if x in "AEIOUaeiou":
            i += 1

    return i


print(st_sam(niz))


def st_so(niz: str) -> int:
    i: int = 0

    for x in niz:
        if x in "qQwWrRtTzZpPšŠsSdDfFgGhHjJkKlLčČxXcCvVbBnNmM":
            i += 1

    return i


print(st_so(niz))
