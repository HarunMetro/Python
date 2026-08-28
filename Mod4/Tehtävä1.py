import math

Kuhan_pituus = float(input("Anna kuhan pituus (cm):\n"))

if Kuhan_pituus >= 37:
    print("Kuhan pituus on riittävä, voit ottaa sen mukaasi.")
else:
    print(f"Kuhan pituus on {37 - Kuhan_pituus:.1f} cm lyhyempi kuin sallittu määrä, laske se takaisin veteen!")

