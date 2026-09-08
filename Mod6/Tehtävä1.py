import random

summa = 0

noppa = int(input("Kuinka monta noppaa heitetään? "))
for i in range(noppa):
    luku = random.randint(1, 6)
    summa = summa + luku # lyhyeksi: summa += luku
print (f"Noppien silmälukujen summa on {summa}.")

