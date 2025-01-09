import os
import time
from fitcheck.repositories.person_repository import PersonRepository
from fitcheck.utils.calculo import Calculo
import matplotlib.pyplot as plt
import pandas as pd 
import env
    




class CalculationGraphController:
    SAVE_GRAPHS_PATH = env.SAVE_GRAPHS_PATH

    def __init__(self, person):
        self._person = person
        self.c = Calculo(self._person)

    def _get_dado_avaliacao(self, avaliacao, dado):
        dic = self._person.to_dict()
        return dic['evaluations'][avaliacao - 1][dado]
    


    def _verifica_tabela_dc(self, av1, av2):
        dados = {}
        data1 = self._get_dado_avaliacao(av1, 'data')

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


        if( av2 is not None and av2 > 0):
            data2 = self._get_dado_avaliacao(av2, 'data')
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
            dados[''] = ['   '] * 9

        return dados
    
    def _verifica_tabela_do(self, av1, av2):
        dados = {}
        data1 = self._get_dado_avaliacao(av1, 'data')


        dados = {
                'DIÂMENTRO ÓSSEO' : ["Biepicondilar úmero" , "Biepicondilar fêmur","Biestilóide"],
                data1: [
                                self._get_dado_avaliacao(av1, 'do_umero'), 
                                self._get_dado_avaliacao(av1, 'do_femur'), 
                                self._get_dado_avaliacao(av1, 'do_biestiloide')]
        }


        if( av2 is not None and av2 > 0):
            data2 = self._get_dado_avaliacao(av2, 'data')
            dados[data2] = [
                        self._get_dado_avaliacao(av2, 'do_umero'), 
                        self._get_dado_avaliacao(av2, 'do_femur'), 
                        self._get_dado_avaliacao(av2, 'do_biestiloide')]
        else:   
            dados[''] = ['   '] * 3

        return dados
    
    def _verifica_tabela_biotipo(self, av1, av2):
        data1 = self._get_dado_avaliacao(av1, 'data')


        dados = {
                'SOMATOTIPOLOGIA' : ["Endomorfia" , "Mesomorfia","Ectomorfia"],
                data1: [
                        self.c.endomorfia(av1), 
                        self.c.mesomorfia(av1), 
                        self.c.ecotomorfia(av1)]
        }


        if( av2 is not None and av2 > 0):
            data2 = self._get_dado_avaliacao(av2, 'data')
            dados[data2] = [
                        self.c.endomorfia(av2), 
                        self.c.mesomorfia(av2), 
                        self.c.ecotomorfia(av2)]
        else:   
            dados[''] = ['   '] * 3

        return dados
    

    def _verifica_tabela_circuferencia(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        d1 = dic[av1 - 1]
        data1 = d1['data']

        dados['CIRCUNFERÊNCIAS'] = [
            "Ombros (circunferência)", "Tórax", "Cintura", "Abdômen", "Quadril", 
            "Braço direito (contraído)", "Braço esquerdo (contraído)", "Antebraço direito", 
            "Antebraço esquerdo", "Coxa direita proximal", "Coxa esquerda proximal", 
            "Coxa direita medial", "Coxa esquerda medial", "Panturrilha direita", "Panturrilha esquerda"
        ]
        
        l1 = [valor for chave, valor in d1.items() if not (chave.startswith('dc') or chave.startswith('do') or chave.startswith('data') or chave.startswith('weight'))]

        dados[data1] = l1

        if av2 is not None and av2 > 0:
            d2 = dic[av2 - 1]
            data2 = d2['data']
            l2 = [valor for chave, valor in d2.items() if not (chave.startswith('dc') or chave.startswith('do') or chave.startswith('data') or chave.startswith('weight'))]
            
            dados[data2] = l2
        else:
            dados[''] = ['   '] * len(l1)

        return dados

    
    def _verifica_tabela_comp_corporal(self, av1, av2):
        dados = {}
        dic = self._person.to_dict()['evaluations']
        d1 = dic[av1 - 1]
        data1 = d1['data']

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

        
        l1 = [self.c.percentual_gordura(av1), self.c.peso_osseo(av1), self.c.peso_residual(av1),
              self.c.massa_corporal_magra(av1), self.c.peso_gordo(av1), self.c.peso_muscular(av1),
              self.c.cal_densidade_corporal(av1), self.c.sum_dobras_cutaneas(av1)    
              ]

        dados[data1] = l1

        if av2 is not None and av2 > 0:
            d2 = dic[av2 - 1]
            data2 = d2['data']
            l2 = [self.c.percentual_gordura(av2), self.c.peso_osseo(av2), self.c.peso_residual(av2),
              self.c.massa_corporal_magra(av2), self.c.peso_gordo(av2), self.c.peso_muscular(av2),
              self.c.cal_densidade_corporal(av2), self.c.sum_dobras_cutaneas(av2)    
              ]
            
            dados[data2] = l2
        else:
            dados[''] = ['   '] * len(l1)

        return dados

    

    def gerar_tabela_d_cutaneas(self, avaliacao1, avaliacao2 = None):
        dados = self._verifica_tabela_dc(avaliacao1, avaliacao2)

        df = pd.DataFrame(dados)

        fig, ax = plt.subplots(figsize=(8, 6)) 
        ax.axis('tight')
        ax.axis('off')

        ax.set_title('Tabela de Dobras Cutâneas', fontsize=22, fontweight='bold', pad=2)

        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        tbl.auto_set_font_size(False)
        tbl.set_fontsize(14) 
        tbl.auto_set_column_width(col=list(range(len(df.columns))))  

        for (row, col), cell in tbl.get_celld().items():
            if row == 0: 
                cell.set_facecolor('#1f77b4') 
                cell.set_text_props(color='white', weight='bold') 
                
            else:
                cell.set_facecolor('#f0f0f0') 
            cell.set_edgecolor('black') 
            cell.set_height(0.06)  
        
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'table_dobras.png' )
        plt.savefig(local, bbox_inches='tight', pad_inches=0.5, dpi=400)

    def gerar_tabela_d_osseo(self, av1, av2 = None):
        if(av1 == None or av1 < 1):
            return
        
        dados = self._verifica_tabela_do(av1, av2)
        

        df = pd.DataFrame(dados)

        fig, ax = plt.subplots(figsize=(8, 6))  
        ax.axis('tight')
        ax.axis('off')

        ax.set_title('Tabela de Diâmetro Ósseo', fontsize=22, fontweight='bold', pad=2)

        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        tbl.auto_set_font_size(False)
        tbl.set_fontsize(14)  
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1f77b4')  
                cell.set_text_props(color='white', weight='bold') 
            else:
                cell.set_facecolor('#f0f0f0')
            cell.set_edgecolor('black')
            cell.set_height(0.06)  
                
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_d_osseo.png' )

        plt.savefig(local, bbox_inches='tight', pad_inches=0.5, dpi=700)

    
    def gerar_tabela_biotipo(self, av1, av2 = None):
        if av1 is None or av1 < 1:
            return
        dados = self._verifica_tabela_biotipo(av1, av2)

        df = pd.DataFrame(dados)

        fig, ax = plt.subplots(figsize=(1, 5)) 
        ax.axis('tight')
        ax.axis('off')

        ax.set_title('Tabela de Somatotipologia', fontsize=22, fontweight='bold', pad=2)

        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        tbl.auto_set_font_size(False)
        tbl.set_fontsize(14)  
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

  
        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1f77b4')  
                cell.set_text_props(color='white', weight='bold')  
            else:
                cell.set_facecolor('#f0f0f0') 
            cell.set_edgecolor('black')  
            cell.set_height(0.06)

        fig.subplots_adjust(top=0.95)
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_biotipo.png' )
       
        plt.savefig(local, bbox_inches='tight', pad_inches=0.5, dpi=500)


    def gerar_tabela_circunferencias(self, av1, av2 = None):
        if av1 is None or av1 < 1:
            return
        dados = self._verifica_tabela_circuferencia(av1, av2)

        df = pd.DataFrame(dados)

        fig, ax = plt.subplots(figsize=(10, 8))
        ax.axis('tight')
        ax.axis('off')

        ax.set_title('Tabela de Circunferências Corporais', fontsize=22, fontweight='bold', pad=50)

        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

   
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(14)  
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1f77b4')  
                cell.set_text_props(color='white', weight='bold')
            else:
                cell.set_facecolor('#f0f0f0') 
            cell.set_edgecolor('black') 
            cell.set_height(0.06)  
                
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_circunferencias.png' )

        plt.savefig(local, bbox_inches='tight', pad_inches=0.5, dpi=400)

    

    def gerar_tabela_comp_corporal(self, av1, av2=0):
        if av1 is None or av1 < 1:
            return
        dados = self._verifica_tabela_comp_corporal(av1, av2)

        # Converter os dados para um DataFrame
        df = pd.DataFrame(dados)

        fig, ax = plt.subplots(figsize=(10, 8))  
        ax.axis('tight')
        ax.axis('off')

        ax.set_title('Tabela de Composição Corporal', fontsize=22, fontweight='bold', pad=2)

        # Criar a tabela
        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Ajustar o estilo da tabela
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(14)  
        tbl.auto_set_column_width(col=list(range(len(df.columns))))  

        for (row, col), cell in tbl.get_celld().items():
            if row == 0: 
                cell.set_facecolor('#1f77b4')  
                cell.set_text_props(color='white', weight='bold') 
            else:
                cell.set_facecolor('#f0f0f0')  
            cell.set_edgecolor('black')  
            cell.set_height(0.06) 
        
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_composicao_corporal.png' )

        plt.savefig(local, bbox_inches='tight', pad_inches=0.5, dpi=700)

        
    def gerar_grafico_pesos(self, av1):
        if av1 is None or av1 < 1:
            return
        # Dados
        labels = ['Peso Gordo', 'Peso Residual', 'Peso Ósseo', 'Peso Muscular', 'Massa Corporal Magra']
        sizes = [self.c.peso_gordo(av1), self.c.peso_residual(av1), self.c.peso_residual(av1), self.c.peso_muscular(av1), self.c.massa_corporal_magra(av1)]
        colors = ['#66b3ff', '#3399ff', '#1a66cc', '#0059b3', '#99ccff']

        
        explode = (0, 0, 0, 0.1, 0)
        plt.figure(figsize=(8,6))
        plt.pie(sizes, labels = labels, autopct='%.1f%%', startangle=90, explode=explode, colors=colors,textprops={'fontweight': 'bold'})
        plt.title('Distribuição de Tipos de Peso', fontsize=16, fontweight='bold')

        plt.savefig('./fitcheck/temp/grafico_pesos.png', bbox_inches='tight', pad_inches=0.1, dpi=600)  
        

    def gerar_grafico_biotipo(self, avaliacao):
        if avaliacao is None or avaliacao < 1:
            return
        
        categorias = ['ENDOMORFIA','MESOMORFIA', 'ECTOMORFIA']
        valores = [self.c.endomorfia(avaliacao), self.c.mesomorfia(avaliacao), self.c.ecotomorfia(avaliacao)]
        plt.bar(categorias, valores, color='blue')
        plt.ylim(0, 8)
        plt.title("Biotipos",fontweight='bold')
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'grafico_biotipo.png' )

        plt.savefig(local)


    def gerar_tabela_informacoes_avaliado(self):
        nome = self._person.name
        altura = self._person.height
        idade = self._person.age()
        genero = self._person.gender

        dados = {
            "Informações": ["Nome", "Altura", "Idade", "Gênero"],
            "Valores": [f"{nome}", f"{altura}m", f"{idade} anos", f"{genero}"]
        }

        # Converter os dados para um DataFrame
        df = pd.DataFrame(dados)

        # Criar a figura para exibir a tabela
        fig, ax = plt.subplots(figsize=(6, len(df) * 1))  
        ax.axis('tight')
        ax.axis('off')

        # Criar a tabela
        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Ajustar o estilo da tabela
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(12)
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1976D2') 
                cell.set_text_props(color='white', weight='bold')  
            else: 
                cell.set_facecolor('#f0f0f0')
            cell.set_edgecolor('black')
            cell.set_height(0.08) 

        fig.subplots_adjust(top=0.9)
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_informacoes_avaliado.png' )

        plt.savefig(local, bbox_inches='tight', dpi=600)

    def gerar_tabela_massa(self, avaliacao1, avaliacao2=None):

        if avaliacao1 is None or avaliacao1 < 1:
            return

        data1 = self._get_dado_avaliacao(avaliacao1, 'data')
        peso1 = self._get_dado_avaliacao(avaliacao1, 'weight')

        dados = [[data1, peso1], ["",""]]
        n = 1.8

        if avaliacao2 is not None and avaliacao2 > avaliacao1:
            peso2 = self._get_dado_avaliacao(avaliacao2, 'weight')
            data2 = self._get_dado_avaliacao(avaliacao2, 'data')
            dados[1] = [data2, peso2]
            n = 1.8

        # Converter os dados para um DataFrame
        df = pd.DataFrame(dados, columns=["Data", "Peso (kg)"])

        # Criar a figura para exibir a tabela
        fig, ax = plt.subplots(figsize=(6, len(df) * n)) 
        ax.axis('tight')
        ax.axis('off')

        # Criar a tabela
        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Ajustar o estilo da tabela
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(12)
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1976D2') 
                cell.set_text_props(color='white', weight='bold') 
            else: 
                cell.set_facecolor('#f0f0f0')  
            cell.set_edgecolor('black') 
            cell.set_height(0.08)  

        fig.subplots_adjust(top=0.9)
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_de_massa.png' )

        plt.savefig(local, bbox_inches='tight', dpi=600)




    def gerar_tabela_imc(self, avaliacao, avaliacao2):
        if avaliacao is None or avaliacao < 1:
            return
        data = self._get_dado_avaliacao(avaliacao, 'data')

        dados = [[f"{data}", self.c.calcular_imc(avaliacao)], ["",""]]

        if(avaliacao2 is not None and avaliacao2 > avaliacao):
            data2 = self._get_dado_avaliacao(avaliacao2, 'data')
            dados[1]=([f"{data2}", self.c.calcular_imc(avaliacao)])


        # Converter os dados para um DataFrame
        df = pd.DataFrame(dados, columns=["Data", "IMC"])

        # Criar a figura para exibir a tabela
        fig, ax = plt.subplots(figsize=(6, len(df) * 1.8)) 
        ax.axis('tight')
        ax.axis('off')

        # Criar a tabela
        tbl = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

        # Ajustar o estilo da tabela
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(12)
        tbl.auto_set_column_width(col=list(range(len(df.columns)))) 

        for (row, col), cell in tbl.get_celld().items():
            if row == 0:  
                cell.set_facecolor('#1976D2') 
                cell.set_text_props(color='white', weight='bold') 
            else: 
                cell.set_facecolor('#f0f0f0')  
            cell.set_edgecolor('black') 
            cell.set_height(0.08)  

        fig.subplots_adjust(top=0.9)
        local = os.path.join(self.SAVE_GRAPHS_PATH, 'tabela_de_imc.png' )

        plt.savefig(local, bbox_inches='tight', dpi=600)

    
    def gerar_todos_graficos_tabelas(self, av1, av2 = None):
        self.gerar_grafico_biotipo(av1)
        time.sleep(1)
        self.gerar_tabela_d_osseo(av1,av2)
        time.sleep(1)
        self.gerar_tabela_d_cutaneas(av1,av2)
        time.sleep(1)
        self.gerar_tabela_biotipo(av1,av2)
        time.sleep(1)
        self.gerar_grafico_pesos(av1)
        time.sleep(1)
        self.gerar_tabela_circunferencias(av1,av2)
        time.sleep(1)
        self.gerar_tabela_comp_corporal(av1,av2)
        time.sleep(1)
        self.gerar_tabela_informacoes_avaliado()
        time.sleep(1)
        self.gerar_tabela_massa(av1,av2)
        time.sleep(1)
        self.gerar_tabela_imc(av1,av2)

    def apagar_temp(self):
        directory_path = self.SAVE_GRAPHS_PATH
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path): 
                os.remove(item_path)  
