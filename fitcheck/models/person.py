import datetime

from fitcheck.models.evaluation import Evaluation

class Person:

    def __init__(self, name, birth_year, height, gender, weight):
        """
        Initializes a person with general attributes.

        Args:
            id (str): Person's ID.
            name (str): Person's name.
            birth_year (int): Person's year of birth.
            height (float): Person's height in meters.
            gender (str): Person's gender ("M" for male, "F" for female).
            weight (float): Person's weight in kg.
        """
        
        self._id = id
        self._name = name
        self._birth_year = birth_year
        self._height = height
        self._gender = str(gender).lower()[0]
        self._weight = weight
        self._evaluations = []

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return datetime.datetime.now().year - self._birth_year
    
    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight
    
    @property
    def height(self):
        return self._height
    
    @property
    def gender(self):
        return self._gender
    
        
    def add_evaluation(self, evaluation):
        self._evaluations.append(evaluation)


    def to_dict(self):
        return {
            "name": self.name,
            "birth_year": self._birth_year,
            "gender": self.gender,
            "height": self._height, 
            "weight": self._weight,
            "evaluations": [evaluation.to_dict() for evaluation in self._evaluations],
        }
    
    
