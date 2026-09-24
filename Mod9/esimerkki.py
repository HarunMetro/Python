## EX 1

# class Pelaaja:
#     def __init__(self, nimi):
#         self.nimi = nimi
#         self.elämät = 3
#         self.kolikot = 0 
#         self.pisteet = 0

# ## or 

# # class Pelaaja:
# #     def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
# #         self.nimi = nimi
# #         self.elämät = elämät
# #         self.kolikot = elämät
# #         self.pisteet = pisteet

# mario = Pelaaja("Mario")

# print(f"Nimi: {mario.nimi}"
#       f"\nElämät: {mario.elämät}"
#       f"\nKolikot: {mario.kolikot}"
#       f"\nPisteet: {mario.pisteet}")


## EX 2

class Merirosvolaiva:
    def __init__(self, nimi, tykkien_määrä, miehistön_määrä, kulta=0):
        self.nimi = nimi 
        self.tykkien_määrä = tykkien_määrä
        self.miehistön_määrä = miehistön_määrä
        self.kulta = kulta

    def löydä_aarre(self, määrä):
        self.kulta += määrä

    def menetä_kulta(self, määrä):
        self.kulta -= määrä
        if self.kulta < 0:
            self.kulta = 0 

laiva = Merirosvolaiva("The Black Pearl", 12, 40)

laiva.löydä_aarre(200)
laiva.löydä_aarre(75)
laiva.menetä_kulta(100)

print(f"Nimi: {laiva.nimi}"
      f"\nTykkien määrä: {laiva.tykkien_määrä}"
      f"\nMiehistön määrä: {laiva.miehistön_määrä}"
      f"\nKulta: {laiva.kulta}")