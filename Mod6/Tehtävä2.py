luku = []

vastaus = (input("Anna luku: "))

while vastaus != "":
    luku.append(float(vastaus))
    vastaus = (input("Anna luku: "))

luku.sort(reverse=True)

print("Luvut suurimmasta pienimpään:")

for i in luku[:5]:
    print(i)