from fitcheck.models.person import Person
from fitcheck.utils.json_manager import JsonManager
from fitcheck.models.evaluation import Evaluation


class PersonRepository:
    def __init__(self):
        self._json_manager = JsonManager()
        self._next_id = self._json_manager.get_total_ids()
        self._persons = {}
        self._load_person()
        
        
    def _load_person(self):
        dic = self._json_manager._users
        for p in dic.values():
            person =  Person(p['name'], p['birth_year'], p['height'], p['gender'])
            d =  p['evaluations']      
            for evoluation in d:
                person.add_evaluation(Evaluation(**evoluation))
            self._persons[p['id']] = person
        


    def add_person(self, person):
        person = person
        person_dic = person.to_dict()
        self._next_id += 1
        self._persons[self._next_id] = person
        person_dic["id"] = self._next_id
        self._json_manager.save_users_to_json(self._next_id, person_dic)
        return self._next_id
     

    def get_all(self):
        return self._persons.values()


    def remove_person(self, id):
        if id in self._persons:
            self._persons.pop(id)
            self._json_manager.remove_person(id)

    
    def get_person(self, id):
        return self._persons[id]
    

    def update_person(self, id, dic):
        self._persons[id].add_evaluation(Evaluation(**dic))
        self._json_manager.update_user_json(id, dic)
