import os
import json
import env


class JsonManager:
    def load_users(self):
        users = {}
        diretorio = env.SAVE_USER_JSON
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            if arquivo.endswith('.json'):
                caminho_arquivo = os.path.join(diretorio, arquivo)
                with open(caminho_arquivo, 'r') as file:
                    dados = json.load(file)
                    users[dados['id']] = dados
        return users


    

    def save_users_to_json(self, id, user):
        diretorio = env.SAVE_USER_JSON
        id = str(id)
        id += ".json"
        caminho_arquivo_saida = os.path.join(diretorio, id)
        
        usuarios_para_salvar = user
        
        with open(caminho_arquivo_saida, 'w') as file:
            json.dump(usuarios_para_salvar, file, indent=4)
        
        

    def remove_person(self, id):

        # Verifica se o arquivo existe e remove
        diretorio = env.SAVE_USER_JSON
        caminho_arquivo = os.path.join(diretorio, f"{id}.json")

        try:
            if os.path.exists(caminho_arquivo):
                os.remove(caminho_arquivo)
                print(f"Arquivo {caminho_arquivo} removido com sucesso.")
            else:
                print(f"Arquivo {caminho_arquivo} n�o encontrado.")
        except Exception as e:
            print(f"Erro ao tentar remover o arquivo {caminho_arquivo}: {e}")



    def get_total_ids(self):
        diretorio = env.SAVE_USER_JSON 
        arquivos_json = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.json')]
        return len(arquivos_json)



    def get_person(self, id):
        """
        Retorna os dados de um usuário a partir do arquivo JSON correspondente ao ID.
        
        :param id: ID do usuário a ser retornado.
        :return: Dicionário com os dados do usuário ou None se não encontrado.
        """
        # Diretório e caminho do arquivo JSON
        diretorio = env.SAVE_USER_JSON
        caminho_arquivo = os.path.join(diretorio, f"{id}.json")

        if not os.path.exists(caminho_arquivo):
            print(f"Arquivo JSON para o ID {id} não encontrado.")
            return None  # Retorna None se o arquivo não existir

        # Lê o conteúdo do arquivo JSON
        try:
            with open(caminho_arquivo, 'r') as file:
                user_data = json.load(file)
            return user_data  # Retorna os dados do usuário
        except json.JSONDecodeError:
            print(f"Erro ao decodificar o arquivo JSON para o ID {id}.")
            return None  # Retorna None se houver erro ao decodificar o JSON

    
    @property
    def users(self):
        return self.load_users()
    
    def update_user_json(self, id, evaluation):
        """
        Adiciona uma nova avaliação à lista de avaliações de um usuário específico e salva no JSON.

        :param id: ID do usuário a ser atualizado.
        :param evaluation: Dicionário com os dados da nova avaliação.
        """
        # Diretório e caminho do arquivo JSON
        diretorio = env.SAVE_USER_JSON
        caminho_arquivo = os.path.join(diretorio, f"{id}.json")

        if not os.path.exists(caminho_arquivo):
            raise FileNotFoundError(f"Arquivo JSON para o ID {id} não encontrado.")

        # Lê o conteúdo do arquivo JSON
        try:
            with open(caminho_arquivo, 'r') as file:
                user_data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError(f"Erro ao decodificar o arquivo JSON para o ID {id}. Verifique o conteúdo do arquivo.")

        # Atualiza as avaliações
        if "evaluations" in user_data and isinstance(user_data["evaluations"], list):
            user_data["evaluations"].append(evaluation)
        else:
            user_data["evaluations"] = [evaluation]  # Cria a lista com a avaliação

        # Salva os dados atualizados no arquivo JSON
        with open(caminho_arquivo, 'w') as file:
            json.dump(user_data, file, indent=4)
