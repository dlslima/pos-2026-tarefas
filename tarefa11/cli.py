import users_wrapper as users

def menu():
    while True:
        print("\n--- CLI Gerenciamento de Usuários ---")
        print("1 - Listar todos usuários")
        print("2 - Ver detalhes de um usuário")
        print("3 - Criar novo usuário")
        print("4 - Atualizar usuário")
        print("5 - Deletar usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista = users.list()

            if lista:
                for u in lista:
                    print(f"{u['id']} - {u['name']}")
            else:
                print("Erro ao listar usuários.")

        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")

            user = users.read(user_id)

            if user:
                print(f"\nNome: {user.get('name')}")
                print(f"Username: {user.get('username')}")
                print(f"Email: {user.get('email')}")
                print(f"Telefone: {user.get('phone')}")
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            nome = input("Nome: ")
            username = input("Username: ")

            confirmacao = input("Deseja criar este usuário? (s/n): ")

            if confirmacao.lower() == "s":
                novo_user = {
                    "name": nome,
                    "username": username
                }

                resultado = users.create(novo_user)

                if resultado:
                    print("Usuário criado com sucesso!")
                    print(resultado)
                else:
                    print("Erro ao criar usuário.")

        elif opcao == "4":
            user_id = input("ID do usuário para atualizar: ")
            novo_nome = input("Novo nome: ")

            dados = {
                "name": novo_nome
            }

            resultado = users.update(user_id, dados)

            if resultado:
                print("Usuário atualizado!")
                print(resultado)
            else:
                print("Erro ao atualizar usuário.")

        elif opcao == "5":
            user_id = input("ID do usuário para deletar: ")

            confirmacao = input("Deseja deletar este usuário? (s/n): ")

            if confirmacao.lower() == "s":
                resultado = users.delete(user_id)

                if resultado:
                    print("Usuário deletado com sucesso!")
                else:
                    print("Erro ao deletar usuário.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()