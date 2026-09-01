import random

salainen_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1-10:\n"))

while arvaus != salainen_luku:
    if arvaus < salainen_luku:
        print("Liian pieni arvaus, yritä uudelleen.")
    elif arvaus > salainen_luku:
        print("Arvaus on liian suuri, yritä uudelleen.")
    arvaus = int(input("Arvaa luku väliltä 1-10:\n"))

print("Onneksi olkoon! Arvasit oikein!")