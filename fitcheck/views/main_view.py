from fitcheck.controllers.main_controller import MainController


def terminal_interface():
    controller = MainController()

    while True:
        print("\n--- FitCheck Terminal Interface ---")
        print("1. Verificar se personal está registrado")
        print("2. Registrar personal")
        print("3. Adicionar pessoa")
        print("4. Listar pessoas")
        print("5. Remover pessoa")
        print("6. Adicionar avaliação para uma pessoa")
        print("7. Mostrar avaliações de uma pessoa")
        print("8. Gerar relatório em PDF")
        print("0. Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            if controller.is_personal():
                print("Personal já registrado.")
            else:
                print("Nenhum personal registrado.")

        elif option == "2":
            name = input("Digite o nome do personal: ")
            controller.add_personal(name)
            print(f"Personal '{name}' registrado com sucesso.")

        elif option == "3":
            name = input("Digite o nome da pessoa: ")
            birth_year = int(input("Digite o ano de nascimento: "))
            height = float(input("Digite a altura (em metros): "))
            gender = input("Digite o gênero (M/F): ")
            person_id = controller.add_person(name, birth_year, height, gender)
            print(f"Pessoa adicionada com ID: {person_id}")

        elif option == "4":
            people = controller.show_people()
            if not people:
                print("Nenhuma pessoa registrada.")
            else:
                print("--- Lista de Pessoas ---")
                for person in people:
                    print(person)

        elif option == "5":
            person_id = int(input("Digite o ID da pessoa a ser removida: "))
            controller.remove_person(person_id)
            print(f"Pessoa com ID {person_id} removida.")

        elif option == "6":
            person_id = int(input("Digite o ID da pessoa: "))
            print("Insira os dados da avaliação:")
            kwargs = {}
            while True:
                key = input("Digite o nome do atributo (ou 'fim' para finalizar): ")
                if key == "fim":
                    break
                value = input(f"Digite o valor para '{key}': ")
                kwargs[key] = value
            controller.add_evaluation_in_person(person_id, **kwargs)
            print("Avaliação adicionada com sucesso.")

        elif option == "7":
            person_id = int(input("Digite o ID da pessoa: "))
            evaluations = controller.show_evaluation_in_person(person_id)
            if not evaluations:
                print("Nenhuma avaliação encontrada.")
            else:
                print("--- Avaliações ---")
                for evaluation in evaluations:
                    print(evaluation)

        elif option == "8":
            person_id = int(input("Digite o ID da pessoa: "))
            eval1 = int(input("Digite o nome da primeira avaliação: "))
            a = input("Você qur uma segunda avaliação? ")
            if(a.lower() == "s"):
                eval2 = int(input("Digite o nome da segunda avaliação (opcional): "))
            else:
                eval2 = None
            controller.create_report_pdf(person_id, eval1, eval2)
            print("Relatório PDF gerado com sucesso.")

        elif option == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    terminal_interface()

