import math

leiviskät = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

leiviskä_naula = leiviskät * 20 + naulat
luodit_naula = leiviskä_naula * 32 + luodit

Grammaksi = luodit_naula * 13.3
kilogrammaksi = int(Grammaksi / 1000)

loput_grammat = Grammaksi % 1000 
# rivi 13 tehty AI avulla en keksinyt miten saada grammat joten otin apua netistä.

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammaksi} kilogrammaa ja {loput_grammat:.2f} grammaa.")