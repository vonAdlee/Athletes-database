from ball import BasketballPlayer, FootballPlayer, BallPlayer
from swimmer import Swimmer
from utils import Utils
from HockeyPlayer import HockeyPlayer




exit = True
athletes = []
filename = None

while exit:

# Menu page

    print("1. Load File")
    print("2. Print Stats")
    print("3. Delete Athlete")
    print("4. Save File")
    print("5. Athlete Info")
    print("6. Display Chart")
    print("7. Exit\n\n")

    
    
    choice = int(input("Enter a choice: "))

# Case for invalid choice

    if choice < 1 or choice > 7:
        print("Wrong input! Please try again\n")

# Case for Loading a file

    elif choice == 1:
        filename = input("Enter file name about the athletes: ")

        try:
            file = open(filename, 'r')

            lines = file.readlines()

            for line in lines:

                line = line.strip()

                if line:
                    athlete = Utils.parse(line)
                    athletes.append(athlete)

            file.close()
            print("Athletes loaded successfully\n")

        except FileNotFoundError:
            print(f'file {filename} not found.\n')



# Printing statistics about the athletes

    elif choice == 2:
        print("Statistics: ")
        print("-------------------")
        print(f"{BasketballPlayer.get_total_athletes()} atheletes\n{HockeyPlayer.get_total_hockey_players()} Hocky Players")
        print(f"{BasketballPlayer.get_total_ball_players()}  Ball Players ({BasketballPlayer.get_total_basketball_players()} Basketball and {FootballPlayer.get_total_football_players()} Football Players)")
        print(f"{Swimmer.get_total_swimmers()} swimmers\n\n")
        

        #Printing endoresments sorted alphabetically

        endorsements = {}
        print("Endoresments:")
        print("-------------------")

        for a in athletes:
            if isinstance(a, BasketballPlayer) or isinstance(a, FootballPlayer):
                endorsement = a.get_endorsement()
                if endorsement != 'N/A':
                    endorsements[endorsement] = endorsements.get(endorsement, 0) + 1    #Check if the endorsement is in the dictionary and increments it by 1

        for brand in sorted(endorsements):    
            print(f"{brand}({endorsements[brand]})")

        print("\n\n")

        # Printing goals scored by players sorted by descending , then by name 

        goals = []

        print("Goals scored:")
        print("-------------------")

        for a in athletes:
            if isinstance(a, HockeyPlayer):
                goals.append(a)

        goals.sort(key= lambda x: (-x.get_goals_scored(), x.get_name()))

        for g in goals:
            print(f"{g.get_goals_scored()} {g.get_name()}")


        # Printing touchdowns by players sorted by descending , then by name

        print("\n\nTouchdowns:")
        print("-------------------")

        touchdowns = []

        for a in athletes:
            if isinstance(a, FootballPlayer):
                touchdowns.append(a)

        touchdowns.sort(key= lambda x: (-x.get_touchdowns(), x.get_name()))

        for t in touchdowns:
            print(f"{t.get_touchdowns()} {t.get_name()}")

        print("\n\n")


    
# Case to delete an athlete

    elif choice == 3:
        deleted_athlete = input("Enter the name of the athlete you would like to delete: ")

        duplicates = [a for a in athletes if a.get_name() == deleted_athlete]               # store name if it matches

        if not duplicates:
            print(f"No athlete found with name {deleted_athlete}.\n\n")                     # No name found

        elif len(duplicates) == 1:
            athletes.remove(duplicates[0])                                                  # Found only one name
            print(f"Athlete {deleted_athlete} deleted successfully.\n\n")

        else:
            print(f"Warning! Multiple athletes named {deleted_athlete} found")              # Found multiple names , press yes to delete
            delete_all = input("Would you like to delete them all? (yes/no):")

            if delete_all == 'yes':
                athletes = [a for a in athletes if a.get_name() != deleted_athlete]         # store in athletes only the name that does not match the deleted one
                print(f"All athletes with name {deleted_athlete} were deleted\n\n")

            else:
                print("Deletion cancelled.\n\n")                                            # deletion cancelled



# Case to save content in file

    elif choice == 4:
        if not filename:
            print("No file has been loaded yet")

        else:
            override = input(f"Would you like to override the content in the memory inside the file {filename}? (yes/no): ")

            if override == 'yes':
                try:
                    file = open(filename, 'w')

                    for a in athletes:
                        file.write(a.__str__() + '\n')

                    print(f'file \'{filename}\' updated successfully')

                except Exception as e:
                    print(f"An error occurred: {e}")
                
                file.close()




# Case to print athlete infos.

    elif choice == 5:
        athlete_name = input("Enter athlete name to see infos: ")

        found = 0

        for a in athletes:
            if a.get_name() == athlete_name:

                if isinstance(a, BasketballPlayer) or isinstance(a, FootballPlayer):

                    a.printStats()
                    a.printEndorsement()
                    found += 1

                else:
                    a.printStats()
                    found += 1

        if found == 0:
            print(f"Athlete {athlete_name} not found")

        print("\n")


        
    elif choice == 6:

        level_1_classes = [HockeyPlayer, BallPlayer, Swimmer]
        leaf_classes = [HockeyPlayer, BasketballPlayer, FootballPlayer, Swimmer]  # all leaf classes
        ballplayer_classes = [BasketballPlayer, FootballPlayer]

        Utils.menu(athletes, level_1_classes, leaf_classes, ballplayer_classes)


# Exit the program

    elif choice == 7:
        exit = False

        print("goodbye")





    