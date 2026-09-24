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

# for loop, jossa käyt autot läpi ja arvot jokaisen kohdalla nopeudenmuutoksen arvon, jolla kutsut kiihdytä() funktiota.
# looppaa niin, että autot kulkee tunnin


