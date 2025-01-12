from cx_Freeze import setup, Executable

# Incluindo arquivos e pastas que devem ser acessíveis
include_files = [
    ("data", "data"),  # Diretório de dados
    ("resultados", "resultados"),  # Diretório de resultados
]

# Configurações para o build
build_options = {
    "packages": [],  # Pacotes extras, caso tenha
    "include_files": include_files,  # Arquivos e diretórios adicionais
}

# Configuração do executável
executables = [
    Executable(
        script="fitcheck/views/main_view.py",  # Substitua pelo caminho correto do arquivo principal
        target_name="FitCheck.exe",  # Nome do executável
    )
]

setup(
    name="FitCheck",
    version="1.0",
    description="Sistema de gerenciamento de avaliações físicas",
    options={"build_exe": build_options},
    executables=executables,
)
