class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykynopeus = 0
        self.kuljettumatka = 0

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}"
      f"\nHuippunopeus: {auto.huippunopeus}"
      f"\nNyky nopeus: {auto.nykynopeus}"
      f"\nKuljettu matka: {auto.kuljettumatka}")