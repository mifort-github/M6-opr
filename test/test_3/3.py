def StejMarec(besedilo):
    stevec = 0  # števec nastavimo na 0, na prvo črko v besedilu
    N = len(besedilo)  # len - število znakov, dolžina niza, besedila
    for i in range(0, N):  # preverimo vsako črko, od N=0 (na levi) do N-1 (na desni)
        zn = besedilo[i]  # črka n i-tem mestu
        if zn in "marec":  # če je črka ena od m, a, r, e ali c
            stevec += 1  # števec povečamo za 1
    return stevec  # rezultat funkcije


def StejMarec2(besedilo):
    i: int = 0
    for x in besedilo:
        if x in "marec":
            i += 1

    return i


besedilo = "Na mirni plaži se je znašel smešen rdeč rakun, ki je užival v mrzli limonadi."
# avtor: ChatGPT
StMa = StejMarec(besedilo)  # 3 rezultat shranimo v StMa
StMa2 = StejMarec2(besedilo)
print("st=" + str(StMa))
print('število črk v ' + besedilo + ', ki so v besedi marec, je ' + str(StMa) + '.')
print(StMa2)
