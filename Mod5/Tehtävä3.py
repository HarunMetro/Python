luku = float(input("Anna luku (Enter lopetus): "))

pienin = float(luku)
suurin = float(luku) 

while luku != "":
    luku = float(luku)
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku
    luku = input("Anna luku (Enter lopetus): ")
print("\nLopetetaan ohjelma.")

print(f"\nPienin luku: {pienin}")
print(f"Suurin luku: {suurin}\n")