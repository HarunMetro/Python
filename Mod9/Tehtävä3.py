class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nykynopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = nykynopeus
        self.kuljettumatka = kuljettumatka

    def kiihdytä (self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

    def kulje(self, tunnit):
        self.kuljettumatka += self.nykynopeus*tunnit

auto = Auto("ABC-123", 142)
auto.kuljettumatka = 2000
auto.kiihdytä(100)
auto.kulje(2)

print(f"Rekisteritunnus: {auto.rekisteritunnus}"
      f"\nHuippunopeus: {auto.huippunopeus}"
      f"\nNyky nopeus: {auto.nykynopeus}"
      f"\nKuljettu matka: {auto.kuljettumatka}")