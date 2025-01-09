from fitcheck.controllers.calculation_graph_controller import CalculationGraphController 
from fitcheck.controllers.pdf_report_controller import PdfReporterController
from fitcheck.controllers.person_controller import PersonController
from fitcheck.utils.personal_manager import PersonalManager as pes


class MainController:
    def __init__(self):
        self.personController = PersonController()
        self._list_people = self.personController.list_people()
        self._pdf_report = PdfReporterController()
    
    def _update_people_list(self):
        self._list_people = self.personController.list_people()

    def  is_personal(self):
        return pes.is_name_saved()
    
    def add_personal(self, name):
        pes.save_name(name)

    def add_person(self, name, birth_year, height, gender):
        id = self.personController.add_person(name, birth_year, height, gender)
        self._update_people_list()
        return id
    
    def show_people(self):
        return self._list_people
    
    def remove_person(self, id):
        self.personController.remove_person(id)
        self._update_people_list()

    def add_evaluation_in_person(self, id, **kwargs):
        self.personController.add_evaluation_in_person(id, **kwargs)

    def show_evaluation_in_person(self, id):
        return self.personController.show_evaluation_in_person(id)

    def create_report_pdf(self, id, evoluation1, evoluation2 = None):
        person = self.personController.get_person(id)

        if person is None:
            return 
        
        cgc = CalculationGraphController(person)
        cgc.gerar_todos_graficos_tabelas(evoluation1, evoluation2)
        self._pdf_report.create_pdf(person.stylized_name())
        cgc.apagar_temp()
    
c = MainController()
c.create_report_pdf(1,1,2)
'''c.create_report_pdf(3,1,2)
c.create_report_pdf(1,1,2)'''

        
