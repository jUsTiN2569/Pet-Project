class pet:
    def __init__(self, hunger, happiness, energy):

        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy

    def Pet_Tracker(self):
        print("\nHi, welcome to my pet tracker app.")
        name = input("What is your pet's name? ")
        while True:
            print("[Options: feed, play, rest, status, exit]")
            ask = input("What would you like to do? ")
            if ask == "feed":
                print(f"\nFed {name}! Hunger decreased.\n")

            elif ask == "play":
                print(f"Played with {name}! Happiness increased, energy decreased.\n")

            elif ask == "rest":
                print(f"{name} has slept soundly! Energy increased.\n")

            elif ask == "status":
                print(f"{name}'s Status: Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}")

            elif ask == "update":
                print(f"Updating {name}'s status, time is going by! Your pet is getting tired and hungry!\n")

            else:
                print("You may have typed something wrong, please retype!\n")
            
        
    if __name__ == "__main__":
        Pet_Tracker()

        
        

    
