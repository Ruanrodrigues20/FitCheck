import os
import json
import env


class JsonManager:
    def __init__(self):
        self._users = dict()
        self._load_users()


    def _load_users(self):
        diretorio = env.SAVE_USER_JSON
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            if arquivo.endswith('.json'):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                with open(caminho_arquivo, 'r') as file:
                    dados = json.load(file)
                    self._users[dados['id']] = dados


    

    def save_users_to_json(self, id, user):
        diretorio = env.SAVE_USER_JSON
        id = str(id)
        id += ".json"
        caminho_arquivo_saida = os.path.join(diretorio, id)
        
        usuarios_para_salvar = user
        
        with open(caminho_arquivo_saida, 'w') as file:
            json.dump(usuarios_para_salvar, file, indent=4)
        

    def remove_person(self, id):
        if id in self._users:
            del self._users[id]
            
            diretorio = env.SAVE_USER_JSON
            caminho_arquivo = os.path.join(diretorio, f"{id}.json")
            
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)


    def get_total_ids(self):
        return len(self._users)

    def get_person(self, id):
        return self._users[id]
    
    @property
    def users(self):
        return self._users
    
    def update_user_json(self, id, evaluation):
        """
        Adiciona uma nova avalia��o � lista de evalutions de um usu�rio espec�fico e salva no JSON.
        
        :param id: ID do usu�rio a ser atualizado.
        :param evaluation: Dicion�rio com os dados da nova avalia��o.
        """
        if id in self._users:
            user_data = self._users[id]
            
            if "evaluations" in user_data and isinstance(user_data["evaluations"], list):
                user_data["evaluations"].append(evaluation)  
            else:
                user_data["evaluations"] = [evaluation]  # Cria a lista com a avalia��o
            
            # Atualiza o arquivo JSON correspondente
            diretorio = env.SAVE_USER_JSON
            caminho_arquivo = os.path.join(diretorio, f"{id}.json")
            
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, 'w') as file:
                    json.dump(user_data, file, indent=4)
            else:
                raise FileNotFoundError(f"Arquivo JSON para o ID {id} n�o encontrado.")
        else:
            raise KeyError(f"Usu�rio com ID {id} n�o encontrado.")
