def gallonat_litraksi(gallonat):
    return gallonat * 3.785

gallonat = float(input("Anna gallon määrä(negatiivinen lopettaa ohjelman):"))

while gallonat >=0:
    litrat = gallonat_litraksi(gallonat)
    print(f"{gallonat} gallona on {litrat:.2f} litraa")
    gallonat = float(input("Anna gallon määrä(negatiivinen lopettaa ohjelman)"))

print("Ohjelma lopetettu")