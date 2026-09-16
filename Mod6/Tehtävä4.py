kaupungit = []

for i in range(5):
    kaupunki = input("Anna kaupunki: ")
    kaupungit.append(kaupunki)
print("\nKaupungit ovat:")

for kaupunki in kaupungit:
    print(f"- {kaupunki}")
