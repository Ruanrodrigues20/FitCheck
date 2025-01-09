from fitcheck.repositories.person_repository import PersonRepository
from fitcheck.models.person import Person
from fitcheck.models.evaluation import Evaluation

class PersonController:
    def __init__(self):
        self._repository = PersonRepository()


    def add_person(self, name, birth_year, height, gender):
        person = Person(name, birth_year, height, gender)
        
        if self._repository.contem_person(person):
            return -1
        
        id = self._repository.add_person(person) 
        return id
    

    def list_people(self):
        people = self._repository.get_all()
        sorted_dict_people = dict(sorted(people.items()))  # Ordena por chave
        list_people = []

        for id, person in sorted_dict_people.items():
            list_people.append(f"{id} - {person.__str__()}")

        return list_people

    

    def remove_person(self, id):
        self._repository.remove_person(id)


    def add_evaluation_in_person(self, id, **kwargs):
        e = Evaluation(**kwargs)        
        self._repository.update_person(id, e)


    def get_person(self, id):
        if(self._repository.contem_person(id)):
            return None

        return self._repository.get_person(id)
    
    def show_evaluation_in_person(self, id):
        person = self._repository.get_person(id)
        if(person is None):
            return
        return person.list_evaluation()




