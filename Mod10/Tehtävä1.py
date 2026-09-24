class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerrros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylos(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerrros:
            self.kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        if uusi_kerros > self.ylin_kerros:
            uusi_kerros = self.ylin_kerros
        elif uusi_kerros < self.alin_kerrros:
            uusi_kerros = self.alin_kerrros

        while self.kerros < uusi_kerros:
            self.kerros_ylos()

        while self.kerros > uusi_kerros:
            self.kerros_alas()

h = Hissi(0, 10)

h.siirry_kerrokseen(100)
h.siirry_kerrokseen(h.alin_kerrros)