from fitcheck.models.person import Person
from fitcheck.utils.csv_manager import CsvManager


class PersonRepository:
    def __init__(self):
        self._csv_manager = CsvManager()
        self._next_id = self._csv_manager.get_total_ids
        self._persons = dict()
        dic = dict(self._csv_manager.get_person)

        for key in dic.keys:
            self._persons[key] = dic[key]
        


    def add_person(self, person):
        self._next_id += 1
        self._persons[self._next_id] = person
        self._csv_manager.add_person(self._next_id, person)
        return self._next_id
     

    def get_all(self):
        return self._persons.values()


    def remove_person(self, id):
        self._persons.pop(id)
        self._csv_manager.remove_person(id)

    
    def get_person(self, id):
        return self._persons[id]
