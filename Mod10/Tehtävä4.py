import random


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


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n{self.nimi} — kilpailun pituus {self.pituus} km")
        print(f"{'Rekisteri':<12} {'Huippunopeus':>13} {'Nopeus':>8} {'Matka (km)':>12}")
        print("-" * 49)
        for auto in self.autot:
            print(
                f"{auto.rekisteritunnus:<12} "
                f"{auto.huippunopeus:>13} "
                f"{auto.nykynopeus:>8} "
                f"{auto.kuljettumatka:>12.1f}"
            )

    def kilpailu_ohi(self):
        return any(auto.kuljettumatka >= self.pituus for auto in self.autot)


autot = [
    Auto(f"ABC-{numero}", random.randint(100, 200))
    for numero in range(1, 11)
]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunteja_kulunut = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja_kulunut += 1
    if tunteja_kulunut % 10 == 0:
        kilpailu.tulosta_tilanne()

