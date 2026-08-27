player_username = input("Enter your username: ")
player_age = int(input("Enter your age: "))

if player_age < 12:
    print("You are too young to play this game.")

if player_age >= 12:
    print(f"Welcome {player_username}! You are {player_age} years old.")