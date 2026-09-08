## harjoitus
# nimet = ["omena", "banaani", "appelsiini", "päärynä"]

# for nimi in nimet:
#     print(f"{nimi}!")

## harjoitus
# for number in range(1, 11):
#     print(f"{number}!", end=" ")

## harjoitus
# for luku in range(2, 21, 2):
#     print(luku, end=" ")

##harjoitus
# summa = 0

# for luku in range(1, 101):
#     summa = summa + luku

# print(summa)

##harjoitus
# luvut = [3, 7, 2, 9, 4, 15, 1]

# for luku in luvut:
#     if luku > 5:
#         print(luku, end=" ")

## harjoitus
# sana = str(input("Anna sana: "))

# for i in range(5):
#     print(sana)

# kaupungit = ["Helsinki", "Espoo", "Vantaa", "Oulu"]
# for kaupunki in kaupungit:
#     print(f"{kaupunki} on kaupunki Suomessa.")

# nimet = []

# etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
# while etunimi != "":
#     nimet.append(etunimi)
#     etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

# for nimi in nimet:
#     print(f"Moi, {nimi}!")

luvut = [3, 8, 2, 10, 5]

for luku in luvut:
    if luku > 5:
        print(f"{luku} on suurempi kuin 5.")