player_username = input("Enter your username: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are too young to play this game.")
    exit() #peli sammuu

print(f"\nWelcome {player_username}! Let's start the game!")

# Reppu on lista - siihen voi lisätä ja siitä voi lukea tavarat for-silmukalla
reppu = ["puhelin", "kuulokkeet", "bussikortti", "3 kirjaa", "eväs", "avaimet"]

# sijainti kertoo missä pelaaja on tällä hetkellä
sijainti = "kotona sängyssä makaamassa"

# valikko on lista - for-silmukka tulostaa sen yhdellä kertaa ei tarvitse toistaa print-rivejä
pää_valikko = ["walking", "bicycle", "bus", "car", "train", "backpack", "location", "quit"]


def tulosta_valikko(): # funktio tulostaa valikon
    print("\nHow do you travel to school today?")
    for vaihtoehto in pää_valikko:
        print("- "+ vaihtoehto)

tulosta_valikko()
komento = input("Enter command: ").lower()

while komento != "quit":
    if komento == "walking":
        print(f"\n{player_username} starts walking to school. The sun is shining and the air is fresh.")
        sijainti = "Walking path"
    elif komento == "bicycle":
        print(f"\n{player_username} opens bicycles lock and starts pedaling.")
        sijainti = "Bicycle path"
    elif komento == "bus":
        print(f"\n{player_username} walks towards the bus stop.")
        sijainti = "Bus stop"
    elif komento == "car":
        print(f"\n{player_username} starts the car and drives towards school.")
        sijainti = "Car"
    elif komento == "train":
        print(f"\n{player_username} walks to the train station.")
        sijainti = "Train"
    elif komento == "backpack":
        print("\nYour backpack contains:")
        for tavara in reppu:
            print("- " + tavara)
    elif komento == "location":
        print(f"\nYou are currently: {sijainti}")
    else:
        print("\nUnknown command. Please try again.")

    tulosta_valikko()
    komento = input("Enter command: ").lower()

print(f"\nThank you for playing, {player_username}! See you next time.")