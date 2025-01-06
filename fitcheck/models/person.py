import datetime

class Person:

    def __init__(self, name, birth_year, height, gender, weight):
        """
        Initializes a person with general attributes.

        Args:
            name (str): Person's name.
            age (int): Person's age.
            weight (float): Person's weight in kg.
            height (float): Person's height in meters.
            gender (str): Person's gender ("M" for male, "F" for female).
            evalutions(list): Person's evaluation
        """
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self.gender = str(gender).lower()[0]
        self.weight = weight
        self.evaluations = []


    @property
    def name(self):
        return self.name
    
    @property
    def age(self):
        return datetime.datetime.now().year - self.birth_year
    
    @property
    def weight(self):
        return self.weight
    
    @property
    def height(self):
        return self.height
    
    @property
    def gender(self):
        return self.gender
    

    @weight.setter
    def weight(self, new_weigt):
        self.weight = new_weigt


    @property
    def gender(self):
        return self.gender
 