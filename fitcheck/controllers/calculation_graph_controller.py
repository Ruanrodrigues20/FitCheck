from fitcheck.models.person import Person
from fitcheck.repositories.person_repository import PersonRepository
from fitcheck.utils.calculo import Calculo
import matplotlib.pyplot as plt
import pandas as pd 
from matplotlib import colors
    




class CalculationGraphController:
    def __init__(self, person):
        self._person = person
        self._calculo = Calculo(person)


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
        peso = dic['evaluations'][avaliacao - 1]['weight']
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
    

    def gerar_grafico_biotipo(self, avaliacao):
        categorias = ['ENDOMORFO','MESOMORFO', 'ECTOMORFO']
        valores = [self.endomorfia(avaliacao), self.mesomorfia(avaliacao), self.ecotomorfia(avaliacao)]
        plt.bar(categorias, valores, color='blue')
        plt.ylim(0, 8)
        plt.title("Biotipos")
        plt.xlabel('Categorias')
        plt.ylabel('Valores')
        plt.savefig('./fitcheck/temp/biotipo.png')

    

        


    def _gerar_tabela(self, tipo, av1, av2):
        if av1 is None or av1 < 1:
            return

        if tipo.lower() == "dc":
            dados = self._verifica_tabela_dc(av1, av2)
        elif tipo.lower() == "do":
            dados = self._verifica_tabela_do(av1, av2)
        elif tipo.lower() == "biotipo":
            dados = self._verifica_tabela_biotipo(av1, av2)
        elif tipo.lower() == "circuferencia":
            dados = self._verifica_tabela_circuferencia(av1, av2)
        elif tipo.lower() == "comp_corporal":
            dados = self._verifica_tabela_comp_corporal(av1, av2)
        else:
            return
        
        # Criar dataframe para a tabela
        df1 = pd.DataFrame(dados)

        # Criar figura para salvar a imagem
        fig, ax = plt.subplots(figsize=(12, 8))  # Aumentando o tamanho da figura para qualidade máxima
        ax.axis('tight')
        ax.axis('off')
        tbl1 = ax.table(cellText=df1.values, colLabels=df1.columns, cellLoc='center', loc='center')

        # Ajustar estilo da tabela
        for key, cell in tbl1.get_celld().items():
            # Mudar a cor de fundo das células (use cores diferentes se desejar)
            if key[0] == 0:  # Linha de cabeçalho
                cell.set_facecolor('#1f77b4')  # Azul para cabeçalhos
                cell.set_text_props(color='white')  # Texto branco
            else:
                cell.set_facecolor('#d3d3d3')  # Cinza claro para células de dados
                cell.set_text_props(color='black')  # Texto preto
            cell.set_fontsize(12)
            cell.set_height(0.08)
            cell.set_edgecolor('black')

        # Ajustar layout para garantir que nada seja cortado
        plt.tight_layout()
        # Salvar a imagem com qualidade máxima (600 dpi)
        plt.savefig(f'./fitcheck/temp/table_{tipo}.png', bbox_inches='tight', pad_inches=0, dpi=500)


    def _verifica_tabela_dc(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        data1 = dic[av1 - 1]['data']

        dados = {
                'Dobras Cutâneas': [
                    'DC Bicipital', 'DC Tricipital', 'DC Subescapular', 
                    'DC Suprailíaca', 'DC Abdominal', 'DC Peitoral', 
                    'DC Axilar média', 'DC Coxa', 'DC Panturrilha medial'],
                data1: [
                                self._get_dado_avaliacao(av1, 'dc_bicipital'), 
                                self._get_dado_avaliacao(av1, 'dc_tricipital'), 
                                self._get_dado_avaliacao(av1, 'dc_subescapular'), 
                                self._get_dado_avaliacao(av1, 'dc_suprailiaca'), 
                                self._get_dado_avaliacao(av1, 'dc_abdominal'), 
                                self._get_dado_avaliacao(av1, 'dc_peitoral'), 
                                self._get_dado_avaliacao(av1, 'dc_axilar'), 
                                self._get_dado_avaliacao(av1, 'dc_coxa'), 
                                self._get_dado_avaliacao(av1, 'dc_panturillha')]
                
        }


        if( av2 > 0):
            data2 = dic[av2 - 1]['data']
            dados[data2] = [
                        self._get_dado_avaliacao(av2, 'dc_bicipital'), 
                        self._get_dado_avaliacao(av2, 'dc_tricipital'), 
                        self._get_dado_avaliacao(av2, 'dc_subescapular'), 
                        self._get_dado_avaliacao(av2, 'dc_suprailiaca'), 
                        self._get_dado_avaliacao(av2, 'dc_abdominal'), 
                        self._get_dado_avaliacao(av2, 'dc_peitoral'), 
                        self._get_dado_avaliacao(av2, 'dc_axilar'), 
                        self._get_dado_avaliacao(av2, 'dc_coxa'), 
                        self._get_dado_avaliacao(av2, 'dc_panturillha')]
        else:   
            dados[''] = [0,0, 0, 0, 0, 0, 0, 0,0]

        return dados
    
    def _verifica_tabela_do(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        data1 = dic[av1 - 1]['data']

        dados = {
                'DIÂMENTRO ÓSSEO' : ["Biepicondilar úmero" , "Biepicondilar fêmur","Biestilóide"],
                data1: [
                                self._get_dado_avaliacao(av1, 'do_umero'), 
                                self._get_dado_avaliacao(av1, 'do_femur'), 
                                self._get_dado_avaliacao(av1, 'do_biestiloide')]
        }


        if( av2 > 0):
            data2 = dic[av2 - 1]['data']
            dados[data2] = [
                        self._get_dado_avaliacao(av2, 'do_umero'), 
                        self._get_dado_avaliacao(av2, 'do_femur'), 
                        self._get_dado_avaliacao(av2, 'do_biestiloide')]
        else:   
            dados[''] = [0,0, 0]

        return dados
    
    def _verifica_tabela_biotipo(self, av1, av2):
        dic = self._person.to_dict()['evaluations']
        data1 = dic[av1 - 1]['data']

        dados = {
                'SOMATOTIPOLOGIA' : ["Endomorfia" , "Mesomorfiar","Ectomorfia"],
                data1: [
                        self.endomorfia(av1), 
                        self.mesomorfia(av1), 
                        self.ecotomorfia(av1)]
        }


        if( av2 > 0):
            data2 = dic[av2 - 1]['data']
            dados[data2] = [
                        self.endomorfia(av2), 
                        self.mesomorfia(av2), 
                        self.ecotomorfia(av2)]
        else:   
            dados[''] = [0,0, 0]

        return dados
    

    def _verifica_tabela_circuferencia(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        d1 = dic[av1 - 1]
        data1 = d1['data']

        # Corrigido: Definindo 'CIRCUNFERÊNCIAS' como uma lista (não uma tupla)
        dados['CIRCUNFERÊNCIAS'] = [
            "Ombros (circunferência)", "Tórax", "Cintura", "Abdômen", "Quadril", 
            "Braço direito (contraído)", "Braço esquerdo (contraído)", "Antebraço direito", 
            "Antebraço esquerdo", "Coxa direita proximal", "Coxa esquerda proximal", 
            "Coxa direita medial", "Coxa esquerda medial", "Panturrilha direita", "Panturrilha esquerda"
        ]
        
        # Extraindo os valores de d1
        l1 = [valor for chave, valor in d1.items() if not (chave.startswith('dc') or chave.startswith('do') or chave.startswith('data') or chave.startswith('weight'))]

        dados[data1] = l1

        if av2 > 0:
            d2 = dic[av2 - 1]
            data2 = d2['data']
            l2 = [valor for chave, valor in d2.items() if not (chave.startswith('dc') or chave.startswith('do') or chave.startswith('data') or chave.startswith('weight'))]
            
            dados[data2] = l2
        else:
            dados[''] = [0] * len(l1)

        return dados

    
    def _verifica_tabela_comp_corporal(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        d1 = dic[av1 - 1]
        data1 = d1['data']

        # Corrigido: Definindo 'CIRCUNFERÊNCIAS' como uma lista (não uma tupla)
        dados['COMPOSIÇÃO CORPORAL'] =  [
                            "Percentual de gordura (%GC)",
                            "Peso ósseo (PO)",
                            "Peso residual (PR)",
                            "Massa corporal magra (MCM)",
                            "Peso gordo (PG)",
                            "Peso muscular (PM)",
                            "Densidade Corporal",
                            "Somatório das Dobras Cutâneas (DC)"
                        ]

        
        # Extraindo os valores de d1
        l1 = [self.percentual_gordura(av1), self.peso_osseo(av1), self.peso_residual(av1),
              self.massa_corporal_magra(av1), self.peso_gordo(av1), self.peso_muscular(av1),
              self.cal_densidade_corporal(av1), self.sum_dobras_cutaneas(av1)    
              ]

        dados[data1] = l1

        if av2 > 0:
            d2 = dic[av2 - 1]
            data2 = d2['data']
            l2 = [self.percentual_gordura(av2), self.peso_osseo(av2), self.peso_residual(av2),
              self.massa_corporal_magra(av2), self.peso_gordo(av2), self.peso_muscular(av2),
              self.cal_densidade_corporal(av2), self.sum_dobras_cutaneas(av2)    
              ]
            
            dados[data2] = l2
        else:
            dados[''] = [0] * len(l1)

        return dados

    

    def gerar_tabela_dc(self, avaliacao1, avaliacao2 = 0):
        if(avaliacao1 == None or avaliacao1 < 1):
            return
        
        self._gerar_tabela('dc', avaliacao1, avaliacao2)

    def gerar_tabela_do(self, av1, av2 = 0):
        if(av1 == None or av1 < 1):
            return
        
        self._gerar_tabela("do", av1, av2)
    
    def gerar_tabela_biotipo(self, av1, av2 = 0):
        if(av1 == None or av1 < 1):
            return
        
        self._gerar_tabela("biotipo", av1, av2)

    def gerar_tabela_circuferencia(self, av1, av2 = 0):
        if(av1 == None or av1 < 1):
            return
        
        self._gerar_tabela("circuferencia", av1, av2)
    

    def gerar_tabela_comp_corporal(self, av1, av2=0):
        if(av1 == None or av1 < 1):
            return
        
        self._gerar_tabela("comp_corporal", av1, av2)

    
    def gerar_grafico_pizza_pesos(self, av1):
        # Dados
        labels = ['Peso Gordo', 'Peso Residual', 'Peso Ósseo', 'Peso Muscular', 'Massa Corporal Magra']
        sizes = [self.peso_gordo(av1), self.peso_residual(av1), self.peso_residual(av1), self.peso_muscular(av1), self.massa_corporal_magra(av1)]
        colors = ['#66b3ff', '#3399ff', '#1a66cc', '#0059b3', '#99ccff']
        
        # Criar gráfico de pizza
        plt.figure(figsize=(8,8))  # Tamanho maior para evitar cortes
        wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        
        # Ajustar fonte para rótulos e porcentagens
        for text in texts + autotexts:
            text.set_fontsize(14)  # Aumentar o tamanho da fonte
            text.set_fontweight('bold')  # Deixar a fonte mais forte

        plt.title('Distribuição de Tipos', fontsize=16, fontweight='bold')  # Aumentar o título

        plt.axis('equal')  # Igualar os eixos para o gráfico ficar circular

        # Ajustar layout para garantir que nada seja cortado
        plt.tight_layout()

        plt.savefig('./fitcheck/temp/grafico_pesos.png', bbox_inches='tight', pad_inches=0.1, dpi=600)  # Qualidade máxima

      


p = PersonRepository()
pes = p.get_person(4)

c = CalculationGraphController(pes)

c.gerar_grafico_biotipo(1)
c.gerar_grafico_pizza_pesos(1)
c.gerar_tabela_biotipo(1,2)
c.gerar_tabela_circuferencia(1,2)
c.gerar_tabela_comp_corporal(1,2)
c.gerar_tabela_dc(1,2)
c.gerar_tabela_do(1,2)
