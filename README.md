# FitCheck

FitCheck é uma aplicação desenvolvida para facilitar a gestão de dados relacionados à saúde e condição física de indivíduos. O projeto oferece funcionalidades como cálculos de gráficos, geração de relatórios em PDF e organização de informações de usuários.

## Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

```
.
├── data
│   ├── 1.json
│   ├── 2.json
│   └── personal
│       └── personal_data.json
├── env.py
├── fitcheck
│   ├── controllers
│   │   ├── calculation_graph_controller.py
│   │   ├── main_controller.py
│   │   ├── pdf_report_controller.py
│   │   └── person_controller.py
│   ├── models
│   │   ├── evaluation.py
│   │   └── person.py
│   ├── repositories
│   │   └── person_repository.py
│   ├── static
│   │   ├── background.png
│   │   ├── corpo.png
│   │   └── icon.png
│   ├── temp
│   ├── utils
│   │   ├── calculo.py
│   │   ├── json_manager.py
│   │   └── personal_manager.py
│   └── views
│       └── main_view.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── resultados
│   └── resultado_Luan_Cassio_de_Oliveira.pdf
├── setup.py
└── tests
    ├── test_calculation_graph_controller.py
    ├── test_csv_manager.py
    └── test_pdf_report_controller.py
```

### Principais Diretórios e Arquivos

- **data/**: Contém os arquivos JSON utilizados como banco de dados.
- **fitcheck/**: Pasta principal do projeto, contendo:
  - **controllers/**: Controladores para cálculos, relatórios e gerenciamento de usuários.
  - **models/**: Modelos de dados, como `Evaluation` e `Person`.
  - **repositories/**: Implementações para acesso e manipulação de dados.
  - **utils/**: Ferramentas auxiliares, como gestão de JSON e cálculos personalizados.
  - **views/**: Interface principal do programa.
  - **static/**: Arquivos estáticos, como imagens.
  - **temp/**: Diretório temporário para arquivos gerados dinamicamente.
- **tests/**: Testes automatizados para garantir a qualidade do código.
- **pyproject.toml**: Configuração do gerenciador de dependências Poetry.
- **setup.py**: Configuração para instalação do pacote.

## Requisitos

- Python 3.12+
- Poetry (para gerênciamento de dependências)

## Instalação
No caso se o seu SO for windows:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/FitCheck.git
   cd FitCheck
   ```

2. Instale as dependências com o Poetry:
   ```bash
   poetry install
   ```

3. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```

4. Configure o caminho do Python no VS Code (opcional):
   - Abra o VS Code.
   - Pressione `Ctrl+Shift+P` e selecione **Python: Select Interpreter**.
   - Escolha o ambiente virtual criado pelo Poetry.

## Uso

1. Execute a interface principal:
   ```bash
   python fitcheck/views/main_view.py
   ```

2. Utilize as funcionalidades disponíveis:
   - Geração de relatórios em PDF.
   - Visualização de gráficos personalizados.
   - Gestão de dados de usuários.

## Testes

Execute os testes automatizados para garantir que o sistema esteja funcionando corretamente:

```bash
pytest tests/
```

## Contribuição

1. Crie um fork do repositório.
2. Crie um branch para suas modificações:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas modificações:
   ```bash
   git push origin minha-feature
   ```
4. Abra um Pull Request no repositório original.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Sinta-se à vontade para sugerir melhorias ou relatar problemas! Ótima jornada com o FitCheck! 🏋️‍♂️

