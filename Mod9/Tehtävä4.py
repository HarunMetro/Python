import random 

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


autot = []
for numero in range(1, 11):
    rekisteritunnus = f"ABC-{numero}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

# Kilpailu jatkuu, kunnes jokin auto on ajanut vähintään 10000 km
while True:
    for auto in autot:
        # 1. Nopeuden muutos (-10 ja +15 väliltä)
        auto.kiihdytä(random.randint(-10, 15))
        # 2. Auto liikkuu yhden tunnin
        auto.kulje(1)

    # Tarkista, onko jokin auto maalissa
    if any(auto.kuljettumatka >= 10000 for auto in autot):
        break

# Lopuksi tulostetaan kaikki autot taulukkona
print(f"\n{'Rekisteri':<12} {'Huippunopeus':>13} {'Nopeus':>8} {'Matka (km)':>12}")
print("-" * 48)
for auto in autot:
    print(
        f"{auto.rekisteritunnus:<12} "
        f"{auto.huippunopeus:>13} "
        f"{auto.nykynopeus:>8} "
        f"{auto.kuljettumatka:>12.1f}"
    )


