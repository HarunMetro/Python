# def tervehdi(tervehdys, kerrat):
#     for i in range(kerrat):
#         print(tervehdys + " " + str(i+1) + ". kerran")
#     return

# tervehdi("Moi", 3)
# tervehdi("Hyvää päivää", 2)

# def neliosumma(eka, toka):
#     ns = eka**2 + toka**2
#     return ns

# luku1 = float(input("Anna ensimmäinen luku: "))
# luku2 = float(input("Anna toinen luku: "))
# tulos = neliosumma(luku1, luku2)
# print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")

# def tervehdi():
#     print("Moi!")

# print("Päivä alkaa tervehdyksellä.")
# tervehdi()
# print(f"Sitten siirrytään muihin asioihin.")

def tervehdi(kerrat):
    for i in range(kerrat):
        print("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
tervehdi(5+4+2)
print("Tervehditään lisää.")
tervehdi(2-1)

