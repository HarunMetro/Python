import random

def heittaa_noppaa(tahkojen_määrä):
    return random.randint(1, tahkojen_määrä)

tahkojen_määrä = int(input("Kuinka monta tahkoa nopassa on?"))

silmäluku = heittaa_noppaa(tahkojen_määrä)
print(f"Heitit {silmäluku}!")

while silmäluku != tahkojen_määrä:
    silmäluku = heittaa_noppaa(tahkojen_määrä)
    print(f"Heitit {silmäluku}!")

print(f"Sait maksimisilmäluvun {tahkojen_määrä}!")