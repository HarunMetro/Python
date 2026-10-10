lentokentat = {}

while True:
    print("\n1) Lisää lentoasema")
    print("2) Hae lentoasema")
    print("3) Lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentokentat[icao] = nimi
        print(f"Lisätty: {icao} - {nimi}")
    
    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentokentat:
            print(f"Lentoasema: {lentokentat[icao]}")
        else:
            print("Lentoasemaa ei löydy")
    
    elif valinta == "3":
        print("Lopetetaan.")
        break
    
    else:
        print("Virheellinen valinta")
