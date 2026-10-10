class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

    def kulje(self, tunnit):
        self.kuljettumatka += self.nykynopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko



sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(120)
sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"{sähköauto.rekisteritunnus}: {sähköauto.kuljettumatka} km")
print(
    f"{polttomoottoriauto.rekisteritunnus}: "
    f"{polttomoottoriauto.kuljettumatka} km"
)