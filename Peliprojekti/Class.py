class Pelaaja:
    def __init__(self, käyttäjätunnus, ikä, tunteet):
        self.käyttäjätunnus = käyttäjätunnus
        self.ikä = ikä
        self.tunteet = []
        self.reppu = [
            Esine("phone", 0.15),
            Esine("headphones", 0.05),
            Esine("bus card", 0.01),
            Esine("3 books", 1.2),
            Esine("lunch", 0.5),
            Esine("keys", 0.1),
        ]
        self.sijainti = Paikka("at home on the couch chilling")
        self.matka_alkanut = False

    def lisää_reppuun(self, nimi, paino=0.1):
        uusi_esine = Esine(nimi, paino)
        self.reppu.append(uusi_esine)

    def lisää_tunteet(self, tunne):
        self.tunteet.append(tunne)
    
    def näytä_reppu(self):
        print("\nYour backpack contains:")
        for esine in self.reppu:
            print(f"- {esine.nimi} ({esine.paino} kg)")

    def näytä_sijainti(self):
        self.näytä_kartta()
        print(f"\nYou are currently: {self.sijainti.nimi}")

    def näytä_kartta(self):
        kartta = """
    ╔═══════════════════════════════════════════════════════╗
    ║                   [  ROUTE MAP  ]                     ║
    ╠═══════════════════════════════════════════════════════╣
    ║                                                       ║
    ║   Walking   Home ●━━●━━●━━●━━●━━●━━●━━─┐              ║
    ║                                        |              ║
    ║   Bicycle   Home ●━━●━━●━━●━━──────────┤              ║
    ║                                        |──▶ SCHOOL    ║
    ║   Bus       Home ●━━●━━●━━●━━●━━───────┤              ║
    ║                                        |              ║
    ║   Car       Home ●━━●━━●━━●━━●━━───────┘              ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
        """
        print(kartta)


def luo_pelaaja():
    käyttäjätunnus = input("Enter username: ")
    käyttäjä_ikä = int(input("Enter age: "))

    if käyttäjä_ikä < 12:
        print("You are too young to play this game, thank you and bye bye.")
        exit()
    elif käyttäjä_ikä > 99:
        print("Your too old to play this game, thank you and bye bye.")
        exit()  # peli sammuu   

    return Pelaaja(käyttäjätunnus, käyttäjä_ikä)

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

class Paikka:
    def __init__(self, nimi):
        self.nimi = nimi