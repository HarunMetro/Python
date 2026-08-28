import math 

sukupuoli = input("Mikä on sinun sukupuoli (mies/nainen):\n")
veriarvo = float(input("Anna hemoglobiiniarvo (g/l):\n"))

if sukupuoli == "mies" and veriarvo < 134:
    print("Hemoglobiiniarvo on alhainen.") 
elif sukupuoli == "mies" and veriarvo >= 134 and veriarvo <= 195:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" and veriarvo > 195:
    print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "nainen" and veriarvo < 117:
    print("Hemoglobiiniarvo on alhainen.")
elif sukupuoli == "nainen" and veriarvo >= 117 and veriarvo <= 175:
    print("Hemoglobiiniarvo on normaali.")
elif sukupuoli == "nainen" and veriarvo > 175:
    print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")