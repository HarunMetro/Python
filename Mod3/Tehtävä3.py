import math

suorakulmion_korkeus = float(input("Kerro suorakulmion korkeus: "))
suorakulmion_leveys = float(input("Kerro suorakulmion leveys: "))

Pinta_ala = suorakulmion_korkeus * suorakulmion_leveys
Piiri = 2 * (suorakulmion_korkeus + suorakulmion_leveys)

print(f"Suorakulmion pinta-ala on {Pinta_ala:.2f} ja piiri on {Piiri:.2f}")
