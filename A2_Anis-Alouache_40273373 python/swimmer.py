from Athlete import Athlete

class Swimmer(Athlete):

    _total_swimmers = 0

    def __init__(self, name=None, age=0, stroke_style = None, country= None, salary = 0, personal_best_time = 0):
        super().__init__(name, age, country, salary)

        self._stroke_style = stroke_style

        if personal_best_time < 0:
            self._personal_best_time = 0
        else:
            self._personal_best_time = personal_best_time

        Swimmer._total_swimmers += 1

        print(f"Swimmer \'{self._name or 'N/A'}\', {self._age or 'N/A'} created; total #of swimmers {Swimmer._total_swimmers}\n")

    
# Set and get Methods

    def get_stroke_style(self):
        return self.get_stroke_style or 'N/A'
    
    def get_personal_best_time(self):
        return f"{self._personal_best_time} minutes"
    
    @staticmethod
    def get_total_swimmers():
        return Swimmer._total_swimmers


    def set_stroke_style(self, stroke_style):
        self._stroke_style = stroke_style

    def set_personal_best_time(self, personal_best_time):
        if personal_best_time < 0:
            self._personal_best_time = 0
        else:
            self._personal_best_time = personal_best_time


# Print stats method

    def printStats(self):
        print(f"Personal best time: {self._personal_best_time} minutes\nStroke style: {self._stroke_style}")    


# Stringify method

    def __str__(self):
        return f"{super().__str__()}, stroke style {self._stroke_style or 'N/A'}, personal best time: {self._personal_best_time} minutes"
    