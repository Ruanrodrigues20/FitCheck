# env.py

import os

# Obter o diret�rio do arquivo executavel
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho para o diretorio para salvar User JSON
SAVE_USER_JSON = os.path.join(base_dir, 'data')
if not os.path.exists(SAVE_USER_JSON):
    os.makedirs(SAVE_USER_JSON)


# Caminho para o diretorio para salvar Personal JSON
SAVE_PERSONAL_JSON = os.path.join(base_dir, 'data', 'personal')
if not os.path.exists(SAVE_PERSONAL_JSON):
    os.makedirs(SAVE_PERSONAL_JSON)


# Caminho para o diretorio para salvar os graficos gerados
SAVE_GRAPHS_PATH = os.path.join(base_dir, 'fitcheck', 'temp')
if not os.path.exists(SAVE_GRAPHS_PATH):
    os.makedirs(SAVE_GRAPHS_PATH)

# Caminho para o diretorio das imagens usadas
STATIC_IMAGES_PATH = os.path.join(base_dir, 'fitcheck', 'static')


# Definir o diretório de resultados
RESULTS_DIR = os.path.join(base_dir, 'resultados')
# Verificar se o diret�rio existe e criar se n�o
if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

