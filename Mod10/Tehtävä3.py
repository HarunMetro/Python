class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        if uusi_kerros > self.ylin_kerros:
            uusi_kerros = self.ylin_kerros
        elif uusi_kerros < self.alin_kerros:
            uusi_kerros = self.alin_kerros

        while self.kerros < uusi_kerros:
            self.kerros_ylos()

        while self.kerros > uusi_kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = [
            Hissi(alin_kerros, ylin_kerros)
            for _ in range(hissien_lukumaara)
        ]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        if not 1 <= hissin_numero <= len(self.hissit):
            raise ValueError("Hissin numero ei vastaa talon hissien lukumäärää.")

        self.hissit[hissin_numero - 1].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(0)


talo = Talo(0, 10, 2)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 8)
print("Palohälytys!")
talo.palohälytys()
