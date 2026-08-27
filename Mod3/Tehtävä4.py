import math

K1 = float(input("Kerro kolme kokonaislukua:\n"))
K2 = float(input("Toinen:\n"))
K3 = float(input("Kolmas:\n"))

summa = K1 + K2 + K3
tulos = K1 * K2 * K3
keskiarvo = summa / 3

print(f"lukujen summa on {summa}, tulo on {tulos} ja keskiarvo on {keskiarvo:.2f}")
