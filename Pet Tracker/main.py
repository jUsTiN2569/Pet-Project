def Pet_Tracker():




    ask = input("What would you like to pick?: ")



    if ask == "feed":
        print("Fed {pet_name}! Hunger decreased.")

    elif ask == "play":
        print("Played with {pet_name}! Happiness increased, energy decreased.")

    elif ask == "rest":
        print("{pet_name} has slept soundly! Energy increased.")

    elif ask == "status":
        print("{pet_name}'s Status:")

    elif ask == "update":
        print("Updating {pet_name}'s status, time is going by! Your pet is getting tired and hungry!")

    else:
        print("You may have typed something wrong, please retype!")