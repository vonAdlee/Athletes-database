from Athlete import Athlete
from abc import abstractmethod


# Ball players class.

class BallPlayer(Athlete):


    _total_ball_players = 0

    def __init__(self, name = None, age=None, country=None, salary=None, team_name=None, jersey_number=None, endorsement=None):
        super().__init__(name, age, country, salary )
        self._team_name = team_name

        if jersey_number < 0:
            self._jersey_number = 0
        else:
            self._jersey_number = jersey_number
        
        self._endorsement = endorsement

        BallPlayer._total_ball_players += 1

        print(f"Ball Player \'{self._name or 'N/A'}\', {self._age or 'N/A'} created; total #of ball players {BallPlayer._total_ball_players}")


    def get_team_name(self):
        return self._team_name or 'N/A'
    
    def get_jersey_number(self):
        return self._jersey_number or 'N/A'
    
    def get_endorsement(self):
        return self._endorsement or 'N/A'
    
    @staticmethod
    def get_total_ball_players():
        return BallPlayer._total_ball_players
    


    def set_team_name(self, team_name):
        self._team_name = team_name

    def set_jersey_number(self, jersey_number):
        if jersey_number < 0:
            self._jersey_number = 0
        else:
            self._jersey_number = jersey_number

    def set_endorsement(self, endorsement):
        self._endorsement = endorsement

    @abstractmethod
    def printEndorsement():
        pass

    @abstractmethod
    def printStats():
        pass

# Stringify method

    def __str__(self):
        return f"{super().__str__()}, team name: {self._team_name or 'N/A'}, jersey number: {self._jersey_number or 'N/A'}, endorsement: {self._endorsement or 'N/A'}"
    


# Basketball players class

class BasketballPlayer(BallPlayer):

    _basket_ball = 0        # Static attributes that holds total number of basketball players

    def __init__(self, name = None , age = 0, team_name = None, jersey_number = 0, country = None, salary = 0, endorsement = None, three_point_pct = 0, rebounds = 0):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)

        if three_point_pct < 0:
            self._three_point_pct = 0
        else:
            self._three_point_pct = three_point_pct
        
        if rebounds < 0:
            self._rebounds = 0
        else:
            self._rebounds = rebounds

        BasketballPlayer._basket_ball += 1 

        print(f"Basketball Player \'{self._name or 'N/A'}\', {self._age or 'N/A'} created; total #of Basketball players {BasketballPlayer._basket_ball}\n")


# Get and Set methods

    def get_three_point_pct(self):
        return self._three_point_pct
    
    def get_rebounds(self):
        return self._rebounds
 
    
    @staticmethod
    def get_total_basketball_players():
        return BasketballPlayer._basket_ball
    
    
    def set_three_point_pct(self, three_point_pct):
        if three_point_pct < 0:
            self._three_point_pct = 0
        else:
            self._three_point_pct = three_point_pct

    def set_rebounds(self, rebounds):
        if rebounds < 0:
            self._rebounds = 0
        else:
            self._rebounds = rebounds

     
    def __str__(self):
        return f"{super().__str__()}, three point pct: {self._three_point_pct or 'N/A'}, rebounds: {self._rebounds or 'N/A'}" 


# Print Stats method

    def printStats(self):
        print(f"Three point pct: {self._three_point_pct} \nrebounds: {self._rebounds}")

# Print endorsement method

    def printEndorsement(self):
        print(f"Endorsement: {self._endorsement or 'N/A'}")
        




#----------------------------------------------------------------------------------------------------------------------------
# Football players class

class FootballPlayer(BallPlayer):

    _total_football_players = 0

    def __init__(self, name = None, age = 0, team_name= None, jersey_number = 0, country = None, salary = 0, endorsement = None, touchdowns = 0, passing_yards = 0):
        super().__init__(name, age, country, salary, team_name, jersey_number, endorsement)

        if touchdowns < 0:
            self._touchdowns = 0
        else:
            self._touchdowns = touchdowns
        
        if passing_yards < 0:
            self._passing_yards = 0
        else:
            self._passing_yards = passing_yards

        FootballPlayer._total_football_players += 1

        print(f"Football Player \'{self._name or 'N/A'}\', {self._age or 'N/A'} created; total #of football players {FootballPlayer._total_football_players}\n")


# Get and Set methods

    def get_touchdowns(self):
        return self._touchdowns
    
    def get_passing_yards(self):
        return self._passing_yards 
    
    @staticmethod
    def get_total_football_players():
        return FootballPlayer._total_football_players
    
    
    def set_touchdowns(self, touchdowns):
        self._touchdowns = touchdowns

    def set_passing_yards(self, passing_yards):
        self._passing_yards = passing_yards




# Stringify method

    def __str__(self):
        return f"{super().__str__()}, touchdowns: {self._touchdowns}, passing yards: {self._passing_yards}"
    
# Print stats method

    def printStats(self):
        print(f"Touchdowns: {self._touchdowns}  \nPassing yards: {self._passing_yards}" )


# Print endorsement method

    def printEndorsement(self):
        print(f"Endorsement: {self._endorsement or 'N/A'}")


# a = FootballPlayer('Anis' , 20, 'Any' )
# a2 = FootballPlayer()




    
