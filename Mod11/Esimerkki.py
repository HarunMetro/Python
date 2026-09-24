
# class Varusmies():
#     def __init__(self, nimi, sukunimi):
#         self.nimi = nimi
#         self.sukunimi = sukunimi

#     def ilmoita_tiedot(self):
#         print(f"{self.nimi} {self.sukunimi}")

# class Miehistö(Varusmies):
#     def __init__(self, nimi, sukunimi, arvo):
#         super().__init__(nimi, sukunimi) 
#         self.arvo = arvo

#     def ilmoita_tiedot(self):
#         super().ilmoita_tiedot()
#         print(f"{self.arvo}")

# class Henkilökunta(Miehistö):
#     def __init__(self, nimi, sukunimi, arvo, tehtävä):
#         super().__init__(nimi, sukunimi, arvo)
#         self.tehtävä = tehtävä

#     def ilmoita_tiedot(self):
#         super().ilmoita_tiedot()
#         print(f"{self.tehtävä}")

# henkilökunta1 = Henkilökunta(
#     input("Anna etunimesi: "),
#     input("Anna sukunimisi: "),
#     input("Anna arvosi: "),
#     input("Anna tehtäväsi")
# )

# henk1 = Henkilökunta(
# "Sofia",
# "Aateli",
# "kenraali",
# "tapa presidentti"
# )

# henk1.ilmoita_tiedot()


# class Isä():
#     def __init__(self, auto):
#         self.auto = auto

# class Äiti():
#     def __init__(self, linna):
#         self.linna = linna

# class Minä(Isä, Äiti):
#     def __init__(self, auto, linna, persoona):
#         Isä.__init__(self, auto)
#         Äiti.__init__(self, linna)
#         self.persoona = persoona

# minä = Minä(
#     "Porsche",
#     "Suomenlinna",
#     "Donald Trump",
# )

# print(minä.auto)
# print(minä.linna)
# print(minä.persoona)

class Adventurer:
    def __init__(self, adventurer_name, hp_point=100, stm=100, atk_dmg=10):
        self.hp_point = hp_point
        self.stm = stm
        self.atk_dmg = atk_dmg
        self.adventurer_name = adventurer_name

    def gain_life(self, healing):
        self.hp_point += healing
        print(f"{self.adventurer_name} gains {healing}")

    def lose_life(self, amount):
        self.hp_point -= amount

        if self.hp_point <= 0:
            print(f"{self.adventurer_name} died!")


class Mage(Adventurer):
    def __init__(self, adventurer_name):
        super().__init__(adventurer_name, hp_point=50, atk_dmg=20)


class Paladin(Adventurer):
    def __init__(self, adventurer_name):
        super().__init__(adventurer_name, hp_point=150, atk_dmg=5)


class Rogue(Adventurer):
    def __init__(self, adventurer_name):
        super().__init__(adventurer_name)


class Party:
    def __init__(self):
        self.members = []

    def add_member(self, adventurer):
        self.members.append(adventurer)
        print(f"{adventurer.adventurer_name} joined the party.")

    def retire_member(self, adventurer):
        if adventurer in self.members:
            self.members.remove(adventurer)
            print(f"{adventurer.adventurer_name} retired from the party.")
        else:
            print(f"{adventurer.adventurer_name} is not in the party.")

    def show_members(self):
        print("Party members:")
        for member in self.members:
            print(member.adventurer_name)

    def show_health(self):
        print("Party health:")
        for member in self.members:
            print(f"{member.adventurer_name}: {member.hp_point} HP")


playerlist = [
    Mage(input("Mage name: ")),
    Paladin(input("Paladin name: ")),
    Rogue(input("Rogue name: ")),
]

for player in playerlist:
    print(player.adventurer_name)

party = Party()

for player in playerlist:
    party.add_member(player)

party.show_members()
print("\n")

party.show_health()
print("\n")

party.retire_member(playerlist[2])
party.show_members()