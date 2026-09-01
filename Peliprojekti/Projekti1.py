player_username = input("Enter your username: ") # lisää että kun kysyy omaa nimeä sen oma nimi tulisi 
player_age = int(input("Enter your age: ")) # ikä myös

if player_age < 12:
    print("You are too young to play this game.")
    exit()
print(f"Welcome {player_username}! Let's start the game!")

print("")

print("\nHow do you travel to school today?")
print("- walking")
print("- bicycle")
print("- bus") 
#print("- repussa") # lisää myös reppu komennon joka kertoo mitä repussa on.
#print("- sijainti") # lisää myös sijainti komennon joka kertoo missä olet.
print("- quit")

## Reppussa on tavaroita mutta voit lisätä siihen tavaroita.
## puhelin, kuulokkeet, bussikortti, 3 kirjaa, evästä, avaimet

## Sijainti myös pitää lisätä. Kun kysyy sijaintia niin kertoo missä se on tai missä vaiheessa
## esim jos on pyörä matkalla niin sijainti olisi pyöräties tai bussi bussities 

komento = input("Enter command: ").lower()

while komento != "quit":
    if komento == "walking":
        print("\nYou start walking to school. The sun is shining and the air is fresh.")
    elif komento == "bicycle":
        print("\nYou ride your bicycle towards school.") # or you unlock lock and start pedaling.
    elif komento == "bus": 
        print("\nYou start walking towards the bus stop.")    
    else:
        print("Unknown command. Please try again.")
    print("\nHow do you travel to school today?")
    print("- walking")
    print("- bicycle")
    print("- bus")
    print("- quit")
    komento = input("Enter command: ").lower()
print("Thank you for playing! See you next time.")
