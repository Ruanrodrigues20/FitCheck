class Evaluation:
    
    def __init__(self, dc_bicipital, dc_tricipital, dc_subescapular, dc_suprailiaca, dc_abdominal, dc_peitoral, dc_axilar, dc_coxa, dc_panturillha, do_umero, do_femur, do_biestiloide, 
                 ombros, torax, cintura, abdomen, quadril, braco_direito, braco_esquerdo, antebraco_direito, antebraco_esquerdo, coxa_dir_proximal, coxa_esq_proximal, coxa_dir_medial, 
                 coxa_esq_medial, panturilha_direita, panturilha_esquerda):
        
        """
        The `Evaluation` class represents body measurement data. All attributes expect `float` values, representing 
        measurements of various parts of the body.

        Attributes:
            dc_bicipital (float): Measurement of the bicipital skinfold.
            dc_tricipital (float): Measurement of the tricipital skinfold.
            dc_subescapular (float): Measurement of the subscapular skinfold.
            dc_suprailiaca (float): Measurement of the suprailiac skinfold.
            dc_abdominal (float): Measurement of the abdominal skinfold.
            dc_peitoral (float): Measurement of the pectoral skinfold.
            dc_axilar (float): Measurement of the axillary skinfold.
            dc_coxa (float): Measurement of the thigh skinfold.
            dc_panturillha (float): Measurement of the calf skinfold.
            do_umero (float): Measurement of the upper arm at the humerus.
            do_femur (float): Measurement of the thigh at the femur.
            do_biestiloide (float): Measurement of the arm at the biestiloid.
            ombros (float): Measurement of the shoulder width.
            torax (float): Measurement of the chest circumference.
            cintura (float): Measurement of the waist circumference.
            abdomen (float): Measurement of the abdomen circumference.
            quadril (float): Measurement of the hip circumference.
            braco_direito (float): Measurement of the right arm.
            braco_esquerdo (float): Measurement of the left arm.
            antebraco_direito (float): Measurement of the right forearm.
            antebraco_esquerdo (float): Measurement of the left forearm.
            coxa_dir_proximal (float): Measurement of the right thigh at the proximal part.
            coxa_esq_proximal (float): Measurement of the left thigh at the proximal part.
            coxa_dir_medial (float): Measurement of the right thigh at the medial part.
            coxa_esq_medial (float): Measurement of the left thigh at the medial part.
            panturilha_direita (float): Measurement of the right calf.
            panturilha_esquerda (float): Measurement of the left calf.
        """
        
        
        self.dc_bicipital = dc_bicipital
        self.dc_tricipital = dc_tricipital
        self.dc_subescapular = dc_subescapular
        self.dc_suprailiaca = dc_suprailiaca
        self.dc_abdominal = dc_abdominal
        self.dc_peitoral = dc_peitoral
        self.dc_axilar = dc_axilar
        self.dc_coxa = dc_coxa
        self.dc_panturillha = dc_panturillha
        self.do_umero = do_umero
        self.do_femur = do_femur
        self.do_biestiloide = do_biestiloide
        self.ombros = ombros
        self.torax = torax
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril
        self.braco_direito = braco_direito
        self.braco_esquerdo = braco_esquerdo
        self.antebraco_direito = antebraco_direito
        self.antebraco_esquerdo = antebraco_esquerdo
        self.coxa_dir_proximal = coxa_dir_proximal
        self.coxa_esq_proximal = coxa_esq_proximal
        self.coxa_dir_medial = coxa_dir_medial
        self.coxa_esq_medial = coxa_esq_medial
        self.panturilha_direita = panturilha_direita
        self.panturilha_esquerda = panturilha_esquerda


    @property
    def dc_bicipital(self):
        return self._dc_bicipital
    
    @dc_bicipital.setter
    def dc_bicipital(self, value):
        self._dc_bicipital = value

    @property
    def dc_tricipital(self):
        return self._dc_tricipital
    
    @dc_tricipital.setter
    def dc_tricipital(self, value):
        self._dc_tricipital = value

    @property
    def dc_subescapular(self):
        return self._dc_subescapular
    
    @dc_subescapular.setter
    def dc_subescapular(self, value):
        self._dc_subescapular = value

    @property
    def dc_suprailiaca(self):
        return self._dc_suprailiaca
    
    @dc_suprailiaca.setter
    def dc_suprailiaca(self, value):
        self._dc_suprailiaca = value

    @property
    def dc_abdominal(self):
        return self._dc_abdominal
    
    @dc_abdominal.setter
    def dc_abdominal(self, value):
        self._dc_abdominal = value

    @property
    def dc_peitoral(self):
        return self._dc_peitoral
    
    @dc_peitoral.setter
    def dc_peitoral(self, value):
        self._dc_peitoral = value

    @property
    def dc_axilar(self):
        return self._dc_axilar
    
    @dc_axilar.setter
    def dc_axilar(self, value):
        self._dc_axilar = value

    @property
    def dc_coxa(self):
        return self._dc_coxa
    
    @dc_coxa.setter
    def dc_coxa(self, value):
        self._dc_coxa = value

    @property
    def dc_panturillha(self):
        return self._dc_panturillha
    
    @dc_panturillha.setter
    def dc_panturillha(self, value):
        self._dc_panturillha = value

    @property
    def do_umero(self):
        return self._do_umero
    
    @do_umero.setter
    def do_umero(self, value):
        self._do_umero = value

    @property
    def do_femur(self):
        return self._do_femur
    
    @do_femur.setter
    def do_femur(self, value):
        self._do_femur = value

    @property
    def do_biestiloide(self):
        return self._do_biestiloide
    
    @do_biestiloide.setter
    def do_biestiloide(self, value):
        self._do_biestiloide = value

    @property
    def ombros(self):
        return self._ombros
    
    @ombros.setter
    def ombros(self, value):
        self._ombros = value

    @property
    def torax(self):
        return self._torax
    
    @torax.setter
    def torax(self, value):
        self._torax = value

    @property
    def cintura(self):
        return self._cintura
    
    @cintura.setter
    def cintura(self, value):
        self._cintura = value

    @property
    def abdomen(self):
        return self._abdomen
    
    @abdomen.setter
    def abdomen(self, value):
        self._abdomen = value

    @property
    def quadril(self):
        return self._quadril
    
    @quadril.setter
    def quadril(self, value):
        self._quadril = value

    @property
    def braco_direito(self):
        return self._braco_direito
    
    @braco_direito.setter
    def braco_direito(self, value):
        self._braco_direito = value

    @property
    def braco_esquerdo(self):
        return self._braco_esquerdo
    
    @braco_esquerdo.setter
    def braco_esquerdo(self, value):
        self._braco_esquerdo = value

    @property
    def antebraco_direito(self):
        return self._antebraco_direito
    
    @antebraco_direito.setter
    def antebraco_direito(self, value):
        self._antebraco_direito = value

    @property
    def antebraco_esquerdo(self):
        return self._antebraco_esquerdo
    
    @antebraco_esquerdo.setter
    def antebraco_esquerdo(self, value):
        self._antebraco_esquerdo = value

    @property
    def coxa_dir_proximal(self):
        return self._coxa_dir_proximal
    
    @coxa_dir_proximal.setter
    def coxa_dir_proximal(self, value):
        self._coxa_dir_proximal = value

    @property
    def coxa_esq_proximal(self):
        return self._coxa_esq_proximal
    
    @coxa_esq_proximal.setter
    def coxa_esq_proximal(self, value):
        self._coxa_esq_proximal = value

    @property
    def coxa_dir_medial(self):
        return self._coxa_dir_medial
    
    @coxa_dir_medial.setter
    def coxa_dir_medial(self, value):
        self._coxa_dir_medial = value

    @property
    def coxa_esq_medial(self):
        return self._coxa_esq_medial
    
    @coxa_esq_medial.setter
    def coxa_esq_medial(self, value):
        self._coxa_esq_medial = value

    @property
    def panturilha_direita(self):
        return self._panturilha_direita
    
    @panturilha_direita.setter
    def panturilha_direita(self, value):
        self._panturilha_direita = value

    @property
    def panturilha_esquerda(self):
        return self._panturilha_esquerda
    
    @panturilha_esquerda.setter
    def panturilha_esquerda(self, value):
        self._panturilha_esquerda = value


    def to_dict(self):
        return {
            "dc_bicipital": self.dc_bicipital,
            "dc_tricipital": self.dc_tricipital,
            "dc_subescapular": self.dc_subescapular,
            "dc_suprailiaca": self.dc_suprailiaca,
            "dc_abdominal": self.dc_abdominal,
            "dc_peitoral": self.dc_peitoral,
            "dc_axilar": self.dc_axilar,
            "dc_coxa": self.dc_coxa,
            "dc_panturillha": self.dc_panturillha,
            "do_umero": self.do_umero,
            "do_femur": self.do_femur,
            "do_biestiloide": self.do_biestiloide,
            "ombros": self.ombros,
            "torax": self.torax,
            "cintura": self.cintura,
            "abdomen": self.abdomen,
            "quadril": self.quadril,
            "braco_direito": self.braco_direito,
            "braco_esquerdo": self.braco_esquerdo,
            "antebraco_direito": self.antebraco_direito,
            "antebraco_esquerdo": self.antebraco_esquerdo,
            "coxa_dir_proximal": self.coxa_dir_proximal,
            "coxa_esq_proximal": self.coxa_esq_proximal,
            "coxa_dir_medial": self.coxa_dir_medial,
            "coxa_esq_medial": self.coxa_esq_medial,
            "panturilha_direita": self.panturilha_direita,
            "panturilha_esquerda": self.panturilha_esquerda
        }

    


'''measurements = {
    "dc_bicipital": 12.3,
    "dc_tricipital": 14.2,
    "dc_subescapular": 15.4,
    "dc_suprailiaca": 13.8,
    "dc_abdominal": 16.5,
    "dc_peitoral": 10.5,
    "dc_axilar": 9.7,
    "dc_coxa": 14.0,
    "dc_panturillha": 11.2,
    "do_umero": 25.6,
    "do_femur": 30.3,
    "do_biestiloide": 26.8,
    "ombros": 45.0,
    "torax": 95.5,
    "cintura": 80.3,
    "abdomen": 85.0,
    "quadril": 100.2,
    "braco_direito": 32.0,
    "braco_esquerdo": 31.5,
    "antebraco_direito": 26.0,
    "antebraco_esquerdo": 25.5,
    "coxa_dir_proximal": 55.0,
    "coxa_esq_proximal": 54.8,
    "coxa_dir_medial": 53.0,
    "coxa_esq_medial": 52.5,
    "panturilha_direita": 37.0,
    "panturilha_esquerda": 36.5
}

evaluation = Evaluation(**measurements)

print(evaluation.to_dict())

'''
