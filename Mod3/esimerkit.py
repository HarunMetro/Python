# # #Muuttujat ja vuorovaikutteiset ohjelmat

# # print('Huommenta, kaikille!\nOlen Harun')

# # user = input("Syötä käyttäjätunnuksesi: ")
# # print("Huomenta", user +"!")

# # Väri = "Punainen"
# # print("Minun suosikki väri on", Väri + ".")

# # eka = -9
# # toka = 12_456_123_180
# # kolmas = 4.973
# # neljäs = -4 + 2j

# # print(eka)
# # print(toka)
# # print(kolmas)
# # print(neljäs)
# # print(neljäs.real)
# # print(neljäs.imag)

# # lämpötila = input("Kerro lämpötila fahrenheit yksikössä:")

# # int_lämpötila = int(lämpötila)
# # celsius = (int(lämpötila) - 32) * 5 / 9

# # print("Lämpötila celsius yksikössä on", (str(celsius))) 
# # #voi myös laittaa vain , celcius se myös toimii, mutta silloin celsius on float eikä string

# # print(f"Lämpötila {int(lämpötila):.3f} Fahrenheit-asteina: {celsius:6.2f}")

# # import math

# # print(f"{'Pii':12s}:{math.pi:10.5f}")
# # print(f"{'Neperin luku':12s}:{math.e:10.5f}")


#example 1 

Pyöreä = float(input("Kerro pyöreän säde: "))
Neliö = float(input("Kerro neliön sivu: "))

import math

pyöreän_pintala = math.pi * (Pyöreä) ** 2
neliön_pintala = Neliö ** 2


print(f"pyöreän pinta-ala on {pyöreän_pintala:.2f} ja neliön pinta-ala on {neliön_pintala:.2f}")

#example 2

import math
import random

banaani = float(input("Kerro banaanin paino kiloina: "))
omena = float(input("Kerro omenan paino kiloina: "))
appelsiini = float(input("Kerro appelsiinin paino kiloina: "))

Banaanin_hinta = banaani*2.85
Omenan_hinta = omena*3.15
Appelsiinin_hinta = appelsiini*4.05
Yhteishinta = Banaanin_hinta + Omenan_hinta + Appelsiinin_hinta

print(f"Banaanin hinta on {Banaanin_hinta:.2f}€, ")
print(f"Omenan hinta on {Omenan_hinta:.2f}€ ")
print(f"Appelsiinin hinta on {Appelsiinin_hinta:.2f}€")
print(f"Yhteensä: {Yhteishinta:.2f}€")

#example 3

import random
import math

Dice1 = random.randint(1, 6)
Dice2 = random.randint(1, 20)

Yhteenlasku = Dice1 + Dice2

print(f"Dice 1: {Dice1}")
print(f"Dice 2: {Dice2}")
print(f"Yhteenlasku: {Yhteenlasku}")