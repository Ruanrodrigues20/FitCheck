import os
import json


class JsonManager:
    def __init__(self):
        self._users = dict()
        self._load_users()


    def _load_users(self):
        diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            if arquivo.endswith('.json'):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                with open(caminho_arquivo, 'r') as file:
                    dados = json.load(file)
                    self._users[dados['id']] = dados


    

    def save_users_to_json(self, id, user):
        diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
        id = str(id)
        id += ".json"
        caminho_arquivo_saida = os.path.join(diretorio, id)
        
        usuarios_para_salvar = user
        
        with open(caminho_arquivo_saida, 'w') as file:
            json.dump(usuarios_para_salvar, file, indent=4)
        

    def remove_person(self, id):
        if id in self._users:
            del self._users[id]
            
            diretorio = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data')
            caminho_arquivo = os.path.join(diretorio, f"{id}.json")
            
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)


    def get_total_ids(self):
        return len(self._users)

    def get_user(self, id):
        return self._users[id]
    
    @property
    def users(self):
        return self._users