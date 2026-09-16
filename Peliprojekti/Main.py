from funktiot import *

käyttäjätunnus = input("Enter your username: ")
käyttäjä_ikä = int(input("Enter your age: "))

if käyttäjä_ikä < 12:
    print("You are too young to play this game, thank you and bye bye.")
    exit()
elif käyttäjä_ikä > 102:
    print("Your too old to play this game, thank you and bye bye.")
    exit()  # peli sammuu

print(f"\nWelcome {käyttäjätunnus}! Let's start the game!")

# valikko on lista for-silmukka tulostaa sen yhdellä kertaa ei tarvitse toistaa print-rivejä
pää_valikko = ["walking", "bicycle", "bus", "car", "backpack", "location", "quit"]
pieni_valikko = ["backpack", "location", "continue", "quit"]

# sijainti kertoo missä pelaaja on tällä hetkellä
sijainti = "at home on the couch chilling"

# reppu on lista siihen voi lisätä ja siitä voi lukea tavarat for-silmukalla
reppu = ["phone", "headphones", "bus card", "3 books", "lunch", "keys"]

tulosta_valikko(pää_valikko, "How do you travel to school today?")
komento = input("Enter command: ").lower()

matka_alkanut = False  

while komento != "quit":
    if not matka_alkanut and komento == "walking":
        reitti_kävely1(käyttäjätunnus,)
        tapahtuma_kävely_roska(käyttäjätunnus, reppu, pieni_valikko)
        tapahtuma_kävely_kyssäri(käyttäjätunnus, reppu, pieni_valikko)
        sijainti = tapahtuma_kävely_ystävä(käyttäjätunnus, reppu, pieni_valikko)
        matka_alkanut = True
    elif not matka_alkanut and komento == "bicycle":
        sijainti = reitti_pyörä1(käyttäjätunnus)
        matka_alkanut = True
    elif not matka_alkanut and komento == "bus":
        sijainti = reitti_bussi1(käyttäjätunnus)
        matka_alkanut = True
    elif not matka_alkanut and komento == "car":
        sijainti = reitti_auto1(käyttäjätunnus)
        matka_alkanut = True
    elif komento == "backpack":
        reppu_tavarat(reppu)
    elif komento == "location":
        print(f"\nYou are currently: {sijainti}")
    else:
        print("\nUnknown command. Please try again.")

    if matka_alkanut:
        tulosta_valikko(pieni_valikko,"Small Menu")
    else:
        tulosta_valikko(pää_valikko, "How do you travel to school today?")
    
    komento = input("Enter command: ").lower()

print(f"\nThank you for playing, {käyttäjätunnus}! See you next time.")