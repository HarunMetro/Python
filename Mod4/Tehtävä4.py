import math

karkaus_vuosi = int(input("Anna vuosi:\n"))

if karkaus_vuosi % 4 == 0:
   if karkaus_vuosi % 100 == 0 and not karkaus_vuosi % 400 == 0:
        print("Vuosi ei ole karkausvuosi.")
    else:
        print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")
    
