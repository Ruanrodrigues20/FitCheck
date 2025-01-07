class Calculo:

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
        peso = self.peso(avaliacao)
        result = peso - (self.peso_gordo(avaliacao) + self.peso_osseo(avaliacao) + self.peso_residual(avaliacao))
        return round(result, 4)

        
    def peso(self, avaliacao):
        dic = self._person.to_dict()
        peso = dic['evaluations'][avaliacao - 1]['peso']
        return peso


    def endomorfia(self, avaliacao):
        dc_subescapular = self._get_dado_avaliacao(avaliacao, 'dc_subescapular' )
        dc_suprailiaca = self._get_dado_avaliacao(avaliacao, 'dc_suprailiaca')
        dc_tricipital = self._get_dado_avaliacao(avaliacao, 'dc_tricipital')
        soma = dc_subescapular + dc_suprailiaca + dc_tricipital
            
        dic = self._person.to_dict()
        altura = dic['height']
        xc = (soma * 170.18) / altura / 100

        endo = 0.1451 * xc - 0.00068 * (xc ** 2) + 0.0000014 * (xc ** 3) - 0.7182
        return round(endo, 4)
        

    def mesomorfia(self, avaliacao):
        do_umero = self._get_dado_avaliacao(avaliacao, 'do_umero')
        do_femur = self._get_dado_avaliacao(avaliacao, 'do_femur') 
        braco_direito = self._get_dado_avaliacao(avaliacao, 'braco_direito')
        dc_tricipital = self._get_dado_avaliacao(avaliacao, 'dc_tricipital')
        coxa_dir_medial = self._get_dado_avaliacao(avaliacao, 'coxa_dir_medial')
        dc_panturillha = self._get_dado_avaliacao(avaliacao, 'dc_panturillha')
            
        dic = self._person.to_dict()
        altura = dic['height'] * 100
            
        #Calculo do perimetro corrigido
        cbc = braco_direito - dc_tricipital
        cpm = coxa_dir_medial - dc_panturillha

        #Calculo do componente
        meso = 0.858 * do_umero + 0.601 * do_femur + 0.188 * cbc + 0.161 * cpm - 0.131 * altura + 4.50
        return round(meso, 4)


    def ecotomorfia(self, avaliacao):
        dic = self._person.to_dict()
        altura = dic['height'] * 100
        peso = self.peso(avaliacao)

        #calculo do indice ponderal
        ip = altura / (peso ** (1/3))

        if(ip > 40.75):
            ecto = (ip * 0.732) - 28.58
            
        elif(38.28 <= ip <= 40.75):
            ecto = (ip * 0.463) - 17.63
        else:
            ecto = 0.1

        return round(ecto,4)



    def _get_dado_avaliacao(self, avaliacao, dado):
        dic = self._person.to_dict()
        return dic['evaluations'][avaliacao - 1][dado]