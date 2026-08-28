import math

karkaus_vuosi = int(input("Anna vuosi:\n"))

if karkaus_vuosi % 4 == 0 or karkaus_vuosi % 400 == 0:
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
    
