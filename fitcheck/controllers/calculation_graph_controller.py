from fitcheck.models.person import Person


class CalculationGraphController:
    def __init__(self, person):
        self._person = person


    def cal_densidade_corporal(self, avaliacao):
        sum_dc = self.sum_dobras_cutaneas(avaliacao)        
        return 1.0970 - (0.0004697 * sum_dc) + 0.00000056 * (sum_dc **2) - (0.00012828 * self._person.age())


    def sum_dobras_cutaneas(self,avaliacao):
        p = self._person.to_dict()
        p = p['evaluations'][avaliacao - 1]
        total = 0
        for key, valor in p.items():
            if key.startswith("dc") and key != "dc_panturillha" and key != "dc_bicipital":  
                total += valor
        return round(total, 4)
    

    def percentual_gordura(self, avaliacao):
        result = ((4.95/self.cal_densidade_corporal(avaliacao)) - 4.5) * 100
        return round(result, 4)
    
    
    def peso_gordo(self, avaliacao):
        dic = self._person.to_dict()
        peso = self.peso(avaliacao)
        result = (peso * (self.percentual_gordura(avaliacao)) / 100)
        return round(result, 4)


    def peso_osseo(self, avaliacao):
        dic = self._person.to_dict()
        altura = dic['height']
        do_biestiloide = dic['evaluations'][avaliacao - 1]['do_biestiloide']
        do_femur = dic['evaluations'][avaliacao - 1]['do_femur']
        result = 3.02 * ((altura ** 2) * do_biestiloide * do_femur * 400) ** (0.712)/1000
        return round(result, 4)


    def peso_residual(self, avaliacao):
        dic = self._person.to_dict()
        peso = self.peso(avaliacao)        
        if(dic['gender'] == "m"):
            result = peso * 0.247
        else:
            result = peso * 0.209

        return round(result, 4)


    def massa_corporal_magra(self, avaliacao):
        peso = self.peso(avaliacao)
        result = peso - self.peso_gordo(avaliacao)
        return round(result, 4)
    

    def peso_muscular(self, avaliacao):
        dic = self._person.to_dict()
        peso = peso = self.peso(avaliacao)
        result = peso - (self.peso_gordo(avaliacao) + self.peso_osseo(avaliacao) + self.peso_residual(avaliacao))
        return round(result, 4)


    def peso(self, avaliacao):
        dic = self._person.to_dict()
        peso = dic['evaluations'][avaliacao - 1]['peso']
        return peso
 
    
