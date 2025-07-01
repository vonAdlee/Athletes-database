from HockeyPlayer import HockeyPlayer
from ball import BasketballPlayer, FootballPlayer, BallPlayer
from swimmer import Swimmer
import matplotlib.pyplot as plt
from collections import Counter

class Utils:

    HockeyPlayer = 'HockeyPlayer'
    BasketballPlayer = 'BasketballPlayer'
    FootballPlayer = 'FootballPlayer'
    Swimmer = 'Swimmer'




    @staticmethod
    def parse(line):

        athlete, data = line.split(":", 1)

        if athlete == Utils.HockeyPlayer:
            infos = data.strip().split(",")

            while len(infos) < 8:      # add missing attributes with none
                infos.append(None)


            name = infos[0]
            age = int(infos[1]) if infos[1] else 0
            country = infos[2]
            salary = float(infos[3]) if infos[3] else 0
            position = infos[4]
            goals_scored = int(infos[5]) if infos[5] else 0
            stick_brand = infos[6]
            skates_size = int(infos[7]) if infos[7] else 0

            return HockeyPlayer(name, age, country, salary, position, goals_scored, stick_brand, skates_size)
        
        elif athlete == Utils.BasketballPlayer:
            infos = data.strip().split(",")

            while len(infos) < 9:      # add missing attributes with none
                infos.append(None)

            name = infos[0]
            age = int(infos[1]) if infos[1] else 0
            team_name = infos[2]
            jersey_number = int(infos[3]) if infos[3] else 0
            country = infos[4]
            salary = float(infos[5]) if infos[5] else 0
            endorsement = infos[6]
            three_point_pct = float(infos[7]) if infos[7] else 0
            rebounds = int(infos[8]) if infos[8] else 0

            return BasketballPlayer(name, age, team_name, jersey_number, country, salary, endorsement, three_point_pct, rebounds)
        
        elif athlete == Utils.FootballPlayer:
            infos = infos = data.strip().split(",")

            while len(infos) < 9:      # add missing attributes with none
                infos.append(None)

            
            name = infos[0]
            age = int(infos[1]) if infos[1] else 0
            team_name = infos[2]
            jersey_number = int(infos[3]) if infos[3] else 0
            country = infos[4]
            salary = float(infos[5]) if infos[5] else 0
            endorsement = infos[6]
            touchdowns = int(infos[7]) if infos[7] else 0
            passing_yards = int(infos[8]) if infos[8] else 0

            return FootballPlayer(name, age, team_name, jersey_number, country, salary, endorsement, touchdowns, passing_yards)
        
        elif athlete ==Utils.Swimmer:
            infos = infos = data.strip().split(",")

            while len(infos) < 6:      # add missing attributes with none
                infos.append(None)


          
            name = infos[0]
            age = int(infos[1]) if infos[1] else 0
            stroke_style = infos[2]
            country = infos[3]
            salary = float(infos[4]) if infos[4] else 0
            personal_best_time = float(infos[5]) if infos[5] else 0

            return Swimmer(name, age, stroke_style, country, salary, personal_best_time)


    @staticmethod
    def plot_pie(data_dict, title):
        if not data_dict:
            print(f"No data to plot for: {title}")
            return
        labels = list(data_dict.keys())
        sizes = list(data_dict.values())

        plt.figure(figsize=(7,7))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.axis('equal')
        plt.show()

    @staticmethod
    def plot_level_1_athlete_counts(athletes, level_1_classes):
        counts = Counter()
        for athlete in athletes:
            for cls in level_1_classes:
                if isinstance(athlete, cls):
                    counts[cls.__name__] += 1
                    break
        Utils.plot_pie(counts, "Number of Athletes (Level 1)")

    @staticmethod
    def plot_leaf_level_athlete_counts(athletes, leaf_classes):
        counts = Counter()
        for athlete in athletes:
            for cls in leaf_classes:
                if isinstance(athlete, cls):
                    counts[cls.__name__] += 1
                    break
        Utils.plot_pie(counts, "Number of Athletes (Leaf Level)")

    @staticmethod
    def plot_level_1_athlete_salaries(athletes, level_1_classes):
        salary_sum = Counter()
        count = Counter()
        for athlete in athletes:
            for cls in level_1_classes:
                if isinstance(athlete, cls) and getattr(athlete, "_salary", None) is not None:
                    salary_sum[cls.__name__] += athlete._salary
                    count[cls.__name__] += 1
                    break
        avg_salary = {k: (salary_sum[k]/count[k]) for k in salary_sum if count[k] > 0}
        Utils.plot_pie(avg_salary, "Average Salary per Athlete Type (Level 1)")

    @staticmethod
    def plot_leaf_level_athlete_salaries(athletes, leaf_classes):
        salary_sum = Counter()
        count = Counter()
        for athlete in athletes:
            for cls in leaf_classes:
                if isinstance(athlete, cls) and getattr(athlete, "_salary", None) is not None:
                    salary_sum[cls.__name__] += athlete._salary
                    count[cls.__name__] += 1
                    break
        avg_salary = {k: (salary_sum[k]/count[k]) for k in salary_sum if count[k] > 0}
        Utils.plot_pie(avg_salary, "Average Salary per Athlete Type (Leaf Level)")

    @staticmethod
    def plot_endorsements(athletes, ballplayer_classes):
        endorsements = Counter()
        for athlete in athletes:
            if any(isinstance(athlete, cls) for cls in ballplayer_classes):
                endorsement = getattr(athlete, "get_endorsement", lambda: 'N/A')()
                if endorsement != 'N/A':
                    endorsements[endorsement] += 1
        Utils.plot_pie(endorsements, "Endorsements Distribution")

    @staticmethod
    def menu(athletes,
             level_1_classes,
             leaf_classes,
             ballplayer_classes):
        while True:
            print("\n--- Athlete Data Charts ---")
            print("1. Number of Athletes (Level 1)")
            print("2. Number of Athletes (Leaf Level)")
            print("3. Athletes Salaries (Level 1)")
            print("4. Athletes Salaries (Leaf Level)")
            print("5. Endorsements")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                Utils.plot_level_1_athlete_counts(athletes, level_1_classes)
            elif choice == '2':
                Utils.plot_leaf_level_athlete_counts(athletes, leaf_classes)
            elif choice == '3':
                Utils.plot_level_1_athlete_salaries(athletes, level_1_classes)
            elif choice == '4':
                Utils.plot_leaf_level_athlete_salaries(athletes, leaf_classes)
            elif choice == '5':
                Utils.plot_endorsements(athletes, ballplayer_classes)
            elif choice == '6':
                print("Exiting chart menu.")
                break
            else:
                print("Invalid choice, please try again.")


        
        

