import json
import os
import env

class PersonalManager:
    SAVE_PATH = env.SAVE_PERSONAL_JSON
    FILE_PATH = os.path.join(SAVE_PATH, 'personal_data.json')

    @classmethod
    def _load_data(cls):
        """Carrega o conte�do do arquivo JSON. Cria um novo arquivo se ele n�o existir."""
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, 'r') as file:
                return json.load(file)
        else:
            # Cria um JSON inicial se o arquivo n�o existir
            return {"Personal": ""}

    @classmethod
    def save_name(cls, name):
        """Salva o nome apenas se a chave 'Personal' estiver vazia."""
        data = cls._load_data()
        if not data.get("Personal"):
            data["Personal"] = name
            os.makedirs(os.path.dirname(cls.FILE_PATH), exist_ok=True)  # Garante que o diret�rio existe
            with open(cls.FILE_PATH, 'w') as file:
                json.dump(data, file, indent=4)
           
    @classmethod
    def is_name_saved(cls):
        """Retorna True se algum nome j� estiver salvo na chave 'Personal', caso contr�rio False."""
        data = cls._load_data()
        return bool(data.get("Personal"))

    @classmethod
    def get_name(cls):
        """Retorna o nome salvo na chave 'Personal'. Retorna None se estiver vazio."""
        data = cls._load_data()
        return data.get("Personal") or None