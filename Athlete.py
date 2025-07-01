from abc import ABC, abstractmethod



class Athlete:

    _total_athletes = 0
 

# Athelete constructor.

    def __init__(self, name=None, age=0, country = None, salary = 0):
        self._name = name 

        if age <= 18:
            self._age = 0
        else:
            self._age = age

        self._country = country

        if salary <= 0:
            self._salary = 0
        else:
            self._salary = salary

        Athlete._total_athletes += 1

        print(f"Athlete \'{self._name or 'N/A'}\' , {self._age or 'N/A'} created; total #of athletes {Athlete._total_athletes}.")


# printStats method (Needs to be overriden)

    @abstractmethod
    def printStats(self):
        pass


# Get and Set methods

    def get_name(self):
        return self._name or 'N/A'
    
    def get_age(self):
        return self._age or 'N/A'
    
    def get_country(self):
        return self._country or 'N/A'

    def get_salary(self):
        return self._salary or 'N/A'
    
    @staticmethod
    def get_total_athletes():
        return Athlete._total_athletes

# Get total athletes "Return for it"
        

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_country(self, country):
        self._country = country

    def set_salary(self, salary):
        self._salary = salary

# Stringify method

    def __str__(self):
      return f"name: {self._name or 'N/A'}, age: {self._age or 'N/A'}, country: {self._country or 'N/A'}, salary: {self._salary or 'N/A'}"  
