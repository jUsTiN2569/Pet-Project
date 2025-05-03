import pet

def Pet_Tracker():
    print("\nHi, welcome to my pet tracker app.")
    name = input("What is your pet's name? ")
    while True:
        print("[Options: feed, play, rest, status, exit]")
        ask = input("What would you like to do? ")
        if ask == "feed":
            print(f"Fed {name}! Hunger decreased.")

        elif ask == "play":
            print(f"Played with {name}! Happiness increased, energy decreased.")

        elif ask == "rest":
            print(f"{name} has slept soundly! Energy increased.")

        elif ask == "status":
            print(f"{name}'s Status:")

        elif ask == "update":
            print(f"Updating {name}'s status, time is going by! Your pet is getting tired and hungry!")

        else:
            print("You may have typed something wrong, please retype!")
        
        
if __name__ == "__main__":
    Pet_Tracker()