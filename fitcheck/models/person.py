import datetime

from fitcheck.models.evaluation import Evaluation

class Person:

    def __init__(self, name, birth_year, height, gender):
        """
        Initializes a person with general attributes.

        Args:
            id (str): Person's ID.
            name (str): Person's name.
            birth_year (int): Person's year of birth.
            height (float): Person's height in meters.
            gender (str): Person's gender ("M" for male, "F" for female).
        """
        
        self._id = id
        self._name = name
        self._birth_year = birth_year
        self._height = height
        self._gender = str(gender).lower()[0]
        self._evaluations = []

    def __str__(self):
        return f"{self._name}, idade: {self.age()}"

    @property
    def name(self):
        return self._name
    
    def age(self):
        return datetime.datetime.now().year - self._birth_year


    
    @property
    def height(self):
        return self._height
    
    @property
    def gender(self):
        return self._gender
    

    def ult_weight(self):
        evo = self._evaluations[-1]
        return evo.weight
    
        
    def add_evaluation(self, evaluation):
        self._evaluations.append(evaluation)


    def to_dict(self):
        return {
            "name": self.name,
            "birth_year": self._birth_year,
            "gender": self.gender,
            "height": self._height, 
            "evaluations": [evaluation.to_dict() for evaluation in self._evaluations],
        }
    
    def ult_evaluation(self):
        n = len(self._evaluations)
        if(n > 1):
            return n, n - 1
        return n
    
    def list_evaluation(self):
        lista = []

        for i in range(len(self._evaluations)):
            lista.append(f"{i} - {self._evaluations[i].__str__()}")
        return lista

    def stylized_name(self):
        return self.name.replace(" ", "_")

    
    
