from fitcheck.repositories.person_repository import PersonRepository
from fitcheck.models.person import Person
from fitcheck.models.evaluation import Evaluation

class PersonController:
    def __init__(self):
        self._repository = PersonRepository()


    def add_person(self, name, birth_year, height, gender, weight):
        person = Person(name, birth_year, height, gender, weight)

        id = self._repository.add_person(person) 
        return id
    

    def list_people(self):
        return self._repository.list_all_person()
    

    def remove_person(self, id):
        self._repository.remove_person(id)


    def add_evaluation_in_person(self, id, **measurable):
        person = self._repository._persons[id]
        evaluation = Evaluation(**measurable)
        person.add_evaluation(evaluation)


    def get_dict_person(self, id):
        person = Person(self._repository.get_person(id))
        return person.to_dict
    
