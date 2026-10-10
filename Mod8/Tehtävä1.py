vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

# Laske indeksin:
if kuukausi >= 12 or kuukausi <= 2:
    # Joulukuu, tammikuu, helmikuu = talvi
    indeksi = 0
elif kuukausi <= 4:
    # Maalis, huhti = kevät
    indeksi = 1
elif kuukausi <= 7:
    # Touko, kesä, heinä = kesä
    indeksi = 2
else:
    # Elo, syys, loka, marras = syksy
    indeksi = 3

print(f"Vuodenaika: {vuodenajat[indeksi]}")
