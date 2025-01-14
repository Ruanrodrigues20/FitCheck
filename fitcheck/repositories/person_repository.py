from fitcheck.models.person import Person
from fitcheck.utils.json_manager import JsonManager
from fitcheck.models.evaluation import Evaluation


class PersonRepository:
    def __init__(self):
        self._json_manager = JsonManager()
        self._next_id = self._json_manager.get_total_ids()
        self._people = {}
        self._load_person()
        
        
    def _load_person(self):
        dic = self._json_manager.load_users()
        for p in dic.values():
            person =  Person(p['name'], p['birth_year'], p['height'], p['gender'])
            d =  p['evaluations']      
            for evoluation in d:
                person.add_evaluation(Evaluation(**evoluation))
            self._people[p['id']] = person
        


    def add_person(self, person):
        person = person
        person_dic = person.to_dict()
        self._next_id += 1
        self._people[self._next_id] = person
        person_dic["id"] = self._next_id
        self._json_manager.save_users_to_json(self._next_id, person_dic)
        return self._next_id
     

    def get_all(self):
        return self._people.copy()


    def remove_person(self, id):
        if id in self._people:
            self._people.pop(id)
            self._json_manager.remove_person(id)

    
    def get_person(self, id):
        if id not in self._people:
            return None

        return self._people[id]
    

    def update_person(self, id, evo):
        self._people[id].add_evaluation(evo)
        self._json_manager.update_user_json(id, evo.to_dict())


    def contem_person(self, person):
        return person in self._people
    
