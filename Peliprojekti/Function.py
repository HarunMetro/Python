from Class import *
import threading

## ajastettu kysymys

def ajastettu_input(kehote, aikaraja=7):
    tulos = [None]

    def kysy():
        tulos[0] = input(kehote)

    threads = threading.Thread(target=kysy)
    threads.daemon = True
    threads.start()
    threads.join(timeout=aikaraja)

    if threads.is_alive():
        return None
    return tulos[0]

## valikko

pää_valikko = "walking", "bicycle", "bus", "car", "backpack", "location", "quit"
pieni_valikko = "backpack", "location", "continue/enter", "quit"

def tulosta_valikko(valikko, otsikko):
    print(f"\n{otsikko}")
    for vaihtoehto in valikko:
        print("- " + vaihtoehto)

def pieni_valikko_lisäys(pelaaja: Pelaaja, pieni_valikko):
    tulosta_valikko(pieni_valikko, "Small menu")
    komento = input("Enter command: ").lower()

    while komento != "continue" and komento != "":
        if komento == "backpack":
            pelaaja.näytä_reppu()
        elif komento == "location":
            pelaaja.näytä_sijainti()
        elif komento == "quit":
            print(f"\nThank you for playing, {pelaaja.käyttäjätunnus}! See you never.")
            exit()
        else:
            print("\n Unknown command. Pleasy try again")
        tulosta_valikko(pieni_valikko, "Small Menu")
        komento = input("Enter command: ").lower()

def aloita_peli(pelaaja: Pelaaja):
    print(f"\nWelcome {pelaaja.käyttäjätunnus}! Let's start the game!")
    tulosta_valikko(pää_valikko, "How would you like to travel to school today?")
    return input("Enter command: ").lower()

## kävely

def reitti_kävely1(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} starts walking to school. The sun is shining and the air is fresh.")
    pelaaja.sijainti = Paikka("Walking path")

def tapahtuma_kävely_roska(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} sees some trash on the ground. Do they want to pick it up? (yes/no)")

    while True:
        valinta_roska = input("Enter your choice: ").lower()

        if valinta_roska == "yes":
            pelaaja.lisää_reppuun("trash")
            print(f"\n{pelaaja.käyttäjätunnus} picks up the trash. Good deed for the day!")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif valinta_roska == "no":
            print(f"\n{pelaaja.käyttäjätunnus} leaves the trash and continues walking.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")


def tapahtuma_kävely_kyssäri(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nDoes {pelaaja.käyttäjätunnus} want to continue walking towards school or change their route to the bus route? (yes/no)")

    while True:
        valinta_kyssäri = input("Enter your choice: ").lower()

        if valinta_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} starts walking towards the bus stop")
            pelaaja.sijainti = Paikka("Bus stop")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif valinta_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} continues walking")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")

def tapahtuma_kävely_ystävä(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} sees their friends in the distance"
    "\n\nDo they want to talk to them? (yes/no)"
    "\nIf they answer 'yes' they will be late for school")

    while True:
        ystävä_kyssäri = input("Enter your choice: ").lower()

        if ystävä_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} starts talking to their friends for 20 minutes")
            tapahtuma_jalkapallo_kutsu(pelaaja, pieni_valikko)
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif ystävä_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} waves at their friends and continues walking to school")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_koira(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")


def tapahtuma_jalkapallo_kutsu(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus}'s friends invite them to play football after school. Do they want to join? (yes/no)")

    while True:
        jalkapallo_kyssäri = input("Enter your choice: ").lower()

        if jalkapallo_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} agrees to play football after school!")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_juoksu(pelaaja, pieni_valikko)
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif jalkapallo_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} declines and continues walking.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_juoksu(pelaaja, pieni_valikko)
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")

def tapahtuma_kävely_juoksu(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} has two options, being late to school or being on time"
        "\n\nIf they run to school the last 1 km they will smell for the rest of the day"
        "\nIf they walk to school their parents will be mad")

    while True:
        kävely_juoksu_kyssäri = input("\nEnter your choice run/walk: ").lower()

        if kävely_juoksu_kyssäri == "walk":
            print(f"\n{pelaaja.käyttäjätunnus} continues walking to school")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif kävely_juoksu_kyssäri == "run":
            print(f"\n{pelaaja.käyttäjätunnus} starts running to school with their heavy backpack")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter run or walk")

def tapahtuma_kävely_koira(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nA friendly dog runs up to {pelaaja.käyttäjätunnus} and starts following them."
          "\nDo they want to pet it? yes/no")

    while True:
        koira_kyssäri = input("Enter your choice: ").lower()

        if koira_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} pets the dog. It wags its tail happily and then runs off.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_oikotie(pelaaja, pieni_valikko)
            return
        elif koira_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} ignores the dog and keeps walking.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_oikotie(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")


def tapahtuma_kävely_oikotie(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} notices a shortcut through the park that could save some time,"
          "\nbut it looks muddy after last night's rain. Take the shortcut? yes/no")

    while True:
        oikotie_kyssäri = input("Enter your choice: ").lower()

        if oikotie_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} takes the shortcut and saves a few minutes, but their shoes get muddy.")
            pelaaja.lisää_reppuun("muddy shoes")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif oikotie_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} sticks to the paved path, keeping their shoes clean.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")

def tapahtuma_kävely_reitti_koulu(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} arrives at school.")

    if any(esine.nimi == "trash" for esine in pelaaja.reppu):
        print(f"A teacher notices {pelaaja.käyttäjätunnus} picking up trash earlier and gives them a compliment!")

    if any(esine.nimi == "muddy shoes" for esine in pelaaja.reppu):
        print(f"{pelaaja.käyttäjätunnus} leaves muddy footprints in the hallway. A janitor gives them a disapproving look.")

    print("\n--- Your journey summary ---")
    if len(pelaaja.reppu) > 6:
        print(f"{pelaaja.käyttäjätunnus} collected quite a few things along the way!")
    else:
        print(f"{pelaaja.käyttäjätunnus} kept their backpack light and simple.")

    print(f"\nThanks for playing, {pelaaja.käyttäjätunnus}! Have a great day at school!")
    exit()

## pyöräily

def reitti_pyörä1(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} opens the bicycle's lock and starts pedaling.")
    pelaaja.sijainti = Paikka("Bicycle path")

def tapahtuma_pyörä_mäki(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nThere's a steep hill ahead. Does {pelaaja.käyttäjätunnus} pedal hard up the hill or take the longer flat road around? (hill/road)")

    while True:
        mäki_kyssäri = input("Enter your choice: ").lower()

        if mäki_kyssäri == "hill":
            print(f"\n{pelaaja.käyttäjätunnus} pedals hard and makes it up the hill, tired but proud.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif mäki_kyssäri == "road":
            print(f"\n{pelaaja.käyttäjätunnus} takes the longer road around. It takes a bit more time but is easy.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter hill or road")


def tapahtuma_pyörä_kivi(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} sees a big rock on the path ahead! Quick, do they swerve to avoid it? (yes/no)")
    print(f"\n{pelaaja.käyttäjätunnus} only has 7 seconds to answer!")

    while True:
        kivi_kyssäri = ajastettu_input("Enter your choice: ", aikaraja=7)

        if kivi_kyssäri is None:
            print(f"\n{pelaaja.käyttäjätunnus} didn't answer in time and hit the rock! Their bicycle breaks.")
            pelaaja.lisää_reppuun("broken bicycle")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_oikotie(pelaaja, pieni_valikko)
            return
        elif kivi_kyssäri.lower() == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} swerves just in time and avoids the rock. Phew!")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif kivi_kyssäri.lower() == "no":
            print(f"\n{pelaaja.käyttäjätunnus} hits the rock head-on! Their bicycle breaks.")
            pelaaja.lisää_reppuun("broken bicycle")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_oikotie(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")


def tapahtuma_pyörä_koira(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nA dog starts chasing {pelaaja.käyttäjätunnus}'s bicycle and barking loudly! Do they pedal faster to escape? (yes/no)")

    while True:
        koira_kyssäri = input("Enter your choice: ").lower()

        if koira_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} pedals as fast as they can and leaves the dog behind.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif koira_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} slows down and the dog bites their leg then wanders off.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")



def tapahtuma_pyörä_reitti_koulu(pelaaja: Pelaaja):
    if "broken bicycle" in pelaaja.reppu:
        print(f"\n{pelaaja.käyttäjätunnus} arrives at school late pushing a broken bicycle.")
        print("Their legs are tired from walking the rest of the way carrying it.")
    else:
        print(f"\n{pelaaja.käyttäjätunnus} arrives at school on the bicycle right on time!")

    print("\n--- Your journey summary ---")
    if len(pelaaja.reppu) > 6:
        print(f"{pelaaja.käyttäjätunnus} collected quite a few things along the way!")
    else:
        print(f"{pelaaja.käyttäjätunnus} kept their backpack light and simple.")

    print(f"\nThanks for playing, {pelaaja.käyttäjätunnus}! Have a great day at school!")

    exit()

## bussi

def reitti_bussi1(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} walks towards the bus stop.")
    pelaaja.sijainti = Paikka("Bus stop")

def tapahtuma_bussi_myöhässä(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nThe bus is running 10 minutes late. Does {pelaaja.käyttäjätunnus} keep waiting or start walking instead? (wait/walk)")
 
    while True:
        myöhässä_kyssäri = input("Enter your choice: ").lower()
 
        if myöhässä_kyssäri == "wait":
            print(f"\nThe bus finally arrives and {pelaaja.käyttäjätunnus} hops on.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif myöhässä_kyssäri == "walk":
            print(f"\n{pelaaja.käyttäjätunnus} decides not to wait any longer and starts walking towards school instead.")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_koira(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter wait or walk")
 
def tapahtuma_bussi_lippu(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} steps onto the bus. Do they tap their bus card? (yes/no)")
 
    while True:
        lippu_kyssäri = input("Enter your choice: ").lower()
 
        if lippu_kyssäri == "yes":
            if any(esine.nimi == "bus card" for esine in pelaaja.reppu):
                print(f"\n{pelaaja.käyttäjätunnus} taps their bus card and finds a seat. Nice and easy.")
            else:
                print(f"\n{pelaaja.käyttäjätunnus} reaches for their bus card but realizes they don't have one!"
                      "\nThey end up paying in coins from the bottom of their backpack.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif lippu_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} sneaks past the driver without paying. Risky move...")
            pelaaja.lisää_tunteet("guilty conscience")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")
 
def tapahtuma_bussi_penkki(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nThe bus is crowded. An elderly passenger gets on and there's only one free seat, {pelaaja.käyttäjätunnus}'s."
          "\nDo they give up their seat? (yes/no)")
 
    while True:
        penkki_kyssäri = input("Enter your choice: ").lower()
 
        if penkki_kyssäri == "yes":
            print(f"\n{pelaaja.käyttäjätunnus} stands up and offers their seat. The passenger thanks them with a warm smile.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif penkki_kyssäri == "no":
            print(f"\n{pelaaja.käyttäjätunnus} pretends to be asleep and keeps their seat. A bit awkward.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter yes or no")
 
def tapahtuma_bussi_pysäkki_ohi(pelaaja: Pelaaja, pieni_valikko):
    print(f"\n{pelaaja.käyttäjätunnus} dozes off listening to music and almost misses their stop!"
          "\nDo they jump off quickly or ride to the next stop? (jump/ride)")
 
    while True:
        ohi_kyssäri = input("Enter your choice: ").lower()
 
        if ohi_kyssäri == "jump":
            print(f"\n{pelaaja.käyttäjätunnus} jumps off just in time, a little dizzy but right where they needed to be.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif ohi_kyssäri == "ride":
            print(f"\n{pelaaja.käyttäjätunnus} rides to the next stop and has to walk back the rest of the way.")
            pelaaja.lisää_tunteet("tired legs")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_oikotie(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter jump or ride")
 
def tapahtuma_bussi_reitti_koulu(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} arrives at school by bus.")
 
    if "guilty conscience" in pelaaja.tunteet:
        print(f"{pelaaja.käyttäjätunnus} still feels a bit bad about not paying for their ticket.")
 
    if "tired legs" in pelaaja.tunteet:
        print("Their legs are still tired from that extra walk after missing their stop.")
 
    print("\n--- Your journey summary ---")
    if len(pelaaja.reppu) > 6:
        print(f"{pelaaja.käyttäjätunnus} collected quite a few things along the way!")
    else:
        print(f"{pelaaja.käyttäjätunnus} kept their backpack light and simple.")
 
    print(f"\nThanks for playing, {pelaaja.käyttäjätunnus}! Have a great day at school!")
    exit()
 
## auto
 
def reitti_auto1(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} starts the car and drives towards school.")
    pelaaja.sijainti = Paikka("Inside car on the road")
 
def tapahtuma_auto_unohdettu(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nHalfway there, {pelaaja.käyttäjätunnus} realizes they forgot their lunch at home!"
          "\nDo they turn back or continue without it? (back/continue)")
 
    while True:
        unohdettu_kyssäri = input("Enter your choice: ").lower()
 
        if unohdettu_kyssäri == "back":
            print(f"\n{pelaaja.käyttäjätunnus} turns back to grab their lunch, losing a few minutes but avoiding a hungry afternoon.")
            if not any(esine.nimi == "lunch" for esine in pelaaja.reppu):
                pelaaja.lisää_reppuun("lunch")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif unohdettu_kyssäri == "continue":
            print(f"\n{pelaaja.käyttäjätunnus} decides to continue without their lunch. Hopefully someone shares with them at school!")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter back or continue")
 
def tapahtuma_auto_liikenne(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nThere's heavy traffic ahead."
          f"\nDoes {pelaaja.käyttäjätunnus} take the highway (slower but safe) or the back roads (faster but risk of getting lost)? (highway/backroads)")
 
    while True:
        liikenne_kyssäri = input("Enter your choice: ").lower()
 
        if liikenne_kyssäri == "highway":
            print(f"\n{pelaaja.käyttäjätunnus} sits patiently in traffic on the highway. Slow but steady.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        elif liikenne_kyssäri == "backroads":
            print(f"\n{pelaaja.käyttäjätunnus} takes the back roads and saves some time, though they did take a wrong turn once.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter highway or backroads")
 
 
def tapahtuma_auto_pysäköinti(pelaaja: Pelaaja, pieni_valikko):
    print(f"\nAll the parking spots near school are full."
          f"\nDoes {pelaaja.käyttäjätunnus} park far away and walk, or circle around to wait for a closer spot? (walk/wait)")
 
    while True:
        pysäköinti_kyssäri = input("Enter your choice: ").lower()
 
        if pysäköinti_kyssäri == "walk":
            print(f"\n{pelaaja.käyttäjätunnus} parks far away and starts walking the rest of the way to school.")
            pelaaja.sijainti = Paikka("Walking path")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            tapahtuma_kävely_juoksu(pelaaja, pieni_valikko)
            return
        elif pysäköinti_kyssäri == "wait":
            print(f"\n{pelaaja.käyttäjätunnus} circles around and finally finds a spot close to school after a few minutes.")
            pieni_valikko_lisäys(pelaaja, pieni_valikko)
            return
        else:
            print("Unkown command. Please enter walk or wait")
 
def tapahtuma_auto_reitti_koulu(pelaaja: Pelaaja):
    print(f"\n{pelaaja.käyttäjätunnus} arrives at school by car.")
 
    print("\n--- Your journey summary ---")
    if len(pelaaja.reppu) > 6:
        print(f"{pelaaja.käyttäjätunnus} collected quite a few things along the way!")
    else:
        print(f"{pelaaja.käyttäjätunnus} kept their backpack light and simple.")
 
    print(f"\nThanks for playing, {pelaaja.käyttäjätunnus}! Have a great day at school!")
    exit()