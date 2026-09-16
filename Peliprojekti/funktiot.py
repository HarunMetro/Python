## valikko
def tulosta_valikko(valikko, otsikko):
    print(f"\n{otsikko}")
    for vaihtoehto in valikko:
        print("- " + vaihtoehto)

def pieni_valikko_lisäys(käyttäjätunnus, reppu, sijainti, pieni_valikko):
    tulosta_valikko(pieni_valikko, "Small menu")
    komento = input("Enter command:").lower()

    while komento != "continue":
        if komento == "backpack":
            reppu_tavarat(reppu)
        elif komento == "location":
            print(f"\nYuo are currently: {sijainti}")
        elif komento == "quit":
            print(f"\nThank you for playing, {käyttäjätunnus}! See you next time.")
            exit()
        else:
            print("\n Unknown command. Pleasy try again")
        tulosta_valikko(pieni_valikko, "Small Menu")
        komento = input("Enter command:").lower()

## kävely 

def reitti_kävely1(käyttäjätunnus):
    print("\nYou start walking to school. The sun is shining and the air is fresh.")
    return "Walking path"

def tapahtuma_kävely_roska(käyttäjätunnus, reppu, pieni_valikko):
    print("\nYou see some trash on the ground. Do you want to pick it up? (yes/no)")

    while True:
        valinta_roska = input("Enter your choice: ").lower()

        if valinta_roska == "yes":
            reppu.append("trash")
            print("\nYou pick up the trash. Good deed for the day!")
            break
        elif valinta_roska == "no":
            print("\nYou leave the trash and continue walking.")
            break
        else:
            print("Unkown command. Please enter yes or no")
        


    pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)

def tapahtuma_kävely_kyssäri(käyttäjätunnus, reppu, pieni_valikko):
    print("\nDo you want to continue walking towards school or change your route to bus route? (yes/no)")

    while True:
        valinta_kyssäri = input("Enter your choice:").lower()

        if valinta_kyssäri == "yes":
            print("\nYou start walking towards bus stop")
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Bus stop", pieni_valikko)
            return "Bus stop"
            break
        elif valinta_kyssäri == "no":
            print("\nYou continue walking")
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)
            return "Walking path"
            break
        else:
            print("Unkown command. Please enter yes or no")
    
def tapahtuma_kävely_ystävä(käyttäjätunnus, reppu, pieni_valikko):
    print("\nYou see your friends in the distance")
    print("\nDo you want to talk to them? (yes/no)")
    print("\nIf you answer 'yes' you will be late for school")

    while True:
        ystävä_kyssäri = input("Enter your choice: ").lower()

        if ystävä_kyssäri == "yes":
            print("\nYou start talking to your friends for 20 minutes")
            tapahtuma_jalkapallo_kutsu(käyttäjätunnus, reppu, pieni_valikko)
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)
            return "Walking path"
            break
        elif ystävä_kyssäri == "no":
            print("\nYou wave at your friends and continue walking to school")
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)
            return "Walking path"
            break
        else:
            print("Unkown command. Please enter yes or no") 


def tapahtuma_jalkapallo_kutsu(käyttäjätunnus, reppu, pieni_valikko):
    print("\nYour friends invite you to play football after school. Do you want to join? (yes/no)")

    while True:
        jalkapallo_kyssäri = input("Enter your choice: ").lower()

        if jalkapallo_kyssäri == "yes":
            print("\nYou agree to play football after school!")
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)
            return "Walking path"
        elif jalkapallo_kyssäri == "no":
            print("\nYou decline and continue walking.")
            pieni_valikko_lisäys(käyttäjätunnus, reppu, "Walking path", pieni_valikko)
            return "Walking path"
        else:
            print("Unkown command. Please enter yes or no") 




## pyöräily

def reitti_pyörä1(käyttäjätunnus):
    print(f"\n{käyttäjätunnus} opens the bicycle's lock and starts pedaling.")
    return "Bicycle path"

## bussi

def reitti_bussi1(käyttäjätunnus):
    print(f"\n{käyttäjätunnus} walks towards the bus stop.")
    return "Bus stop"

## auto

def reitti_auto1(käyttäjätunnus):
    print(f"\n{käyttäjätunnus} starts the car and drives towards school.")
    return "Inside car on the road"

## reppu

def reppu_tavarat(reppu):
    print("\nYour backpack contains:")
    for tavara in reppu:
        print("- " + tavara)