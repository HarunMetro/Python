class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    print()
    hytti_nro_6.tulosta_tiedot()