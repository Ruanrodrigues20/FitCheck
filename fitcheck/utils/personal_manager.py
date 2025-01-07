import json
import os

class PersonalManager:
    FILE_PATH = "./data/personal/personal_data.json"

    @classmethod
    def _load_data(cls):
        """Carrega o conteúdo do arquivo JSON. Cria um novo arquivo se ele não existir."""
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, 'r') as file:
                return json.load(file)
        else:
            # Cria um JSON inicial se o arquivo não existir
            return {"Personal": ""}

    @classmethod
    def save_name(cls, name):
        """Salva o nome apenas se a chave 'Personal' estiver vazia."""
        data = cls._load_data()
        if not data.get("Personal"):
            data["Personal"] = name
            os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)  # Garante que o diretório existe
            with open(cls.FILE_PATH, 'w') as file:
                json.dump(data, file, indent=4)
           

    @classmethod
    def is_name_saved(cls, name):
        """Retorna True se o nome fornecido já estiver salvo na chave 'Personal', caso contrário False."""
        data = cls._load_data()
        return data.get("Personal") == name

    @classmethod
    def get_name(cls):
        """Retorna o nome salvo na chave 'Personal'. Retorna None se estiver vazio."""
        data = cls._load_data()
        return data.get("Personal") or None


# Uso do PersonalManager sem instanciar
PersonalManager.save_name("Ruan Rodrigues da Silva")  # Salvar o nome
