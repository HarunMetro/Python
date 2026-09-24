class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettumatka = 0

    def kiihdytä (self, muutos):
        self.nykynopeus += muutos
        if self.nykynopeus > self.huippunopeus:
            self.nykynopeus = self.huippunopeus
        elif self.nykynopeus < 0:
            self.nykynopeus = 0

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}"
      f"\nHuippunopeus: {auto.huippunopeus}"
      f"\nNyky nopeus: {auto.nykynopeus}"
      f"\nKuljettu matka: {auto.kuljettumatka}")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Nopeus kiihdytysten jälkeen: {auto.nykynopeus}")

auto.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nykynopeus}")
