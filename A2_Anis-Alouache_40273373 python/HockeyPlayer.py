from Athlete import Athlete
from enum import Enum

class HockeyPosition(Enum):
    FORWARD = "forward"
    DEFENSEMAN = "defenseman"
    GOALIE = "goalie" 

class HockeyPlayer(Athlete):

    _total_hockey_player = 0

    def __init__(self, name=None , age=0, country = None, salary = 0, position = None, goals_scored = 0, stick_brand = None, skates_size = None):
        super().__init__(name, age, country, salary)

        if position:
            self._position = HockeyPosition[position.upper()]
        else:
            self._position = None

        if goals_scored < 0:
            self._goals_scored= 0
        else:
            self._goals_scored = goals_scored

        self._stick_brand = stick_brand
        self._skates_size = skates_size

        HockeyPlayer._total_hockey_player += 1

        print(f"Hockey Player \'{self._name or 'N/A'}\', {self._age or 'N/A'} created; total #of hockey players {HockeyPlayer._total_hockey_player}.\n")

# Get and Set methods

    def get_position(self):
        return self._position.value or 'N/A'
    
    def get_goals_scored(self):
        return self._goals_scored
    
    def get_stick_brand(self):
        return self._stick_brand or 'N/A'
    
    def get_skates_size(self):
        return self._skates_size or 'N/A'
    
    @staticmethod
    def get_total_hockey_players():
        return HockeyPlayer._total_hockey_player
    

    def set_position(self, position):
        if position:
            self._position = HockeyPosition[position.upper()]
        else:
            self._position = None

    def set_goals_scored(self, goals_scored):
        if goals_scored < 0:
            self._goals_scored= 0
        else:
            self._goals_scored = goals_scored

    def set_stick_brand(self, stick_brand):
        self._stick_brand = stick_brand

    def set_skates_size(self, skates_size):
        self._skates_size = skates_size

    
# print stats method

    def printStats(self):
        print(f"Position: {self._position.value or 'N/A'}\nGoals scored: {self._goals_scored}")


# Stringify method

    def __str__(self):
        return f"{super().__str__()}, position: {self._position.value or 'N/A'}, goals scored: {self._goals_scored}, stick brand: {self._stick_brand or 'N/A'}, skates size: {self._skates_size or 'N/A'}.\n"






