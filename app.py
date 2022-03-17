from classe_APP import Aplicativo

app = Aplicativo()

print('#'*68)
print("Olá, eu sou o aplicativo de gerenciamento de usuário e suas câmeras!")
print('#'*68)

while True:
    print("1 - Opções de Usuários")
    print("2 - Opções de Câmeras")
    print("0 - Sair")
    try:
        opcao = int(input('Sua escolha: '))
    except:
        print("Digite um valor numérico!")
        continue

    if opcao == 0:
        app.fechar()
        break
    elif opcao == 1:
        while True:
            print("1 - Criar um usuário;")
            print("2 - Atualizar um usuário cadastrado;")
            print("3 - Excluir um usuário cadastrado;")
            print("4 - Listar os usuários cadastrados(Apenas Administradores);")
            print("5 - Buscar um usuário cadastrado(Apenas Administradores);")
            print("0 - Voltar")

            try:
                opcao = int(input('Sua escolha: '))
            except:
                print("Digite um valor numérico!")
                continue

            if opcao == 0:
                break

            elif opcao == 1:
                nome = input("Digite seu nome completo: ").strip()
                email = input("Digite seu email: ").strip()
                dia = input("Dia do seu nascimento: ").strip()
                mes = input("Mês do seu nascimento(Número): ").strip()
                ano = input("Ano do seu nascimento: ").strip()
                data_nascimento = ano+'-'+mes+'-'+dia
                senha = input("Digite sua senha: ").strip()
                senha_c = input("Confirme sua senha: ").strip()

                while True:
                    if senha != senha_c:
                        print("Senhas não correspondem, digite novamente")
                        senha = input("Digite sua senha: ").strip()
                        senha_c = input("Confirme sua senha: ").strip()
                    elif not app.checa_senha(senha):
                        print(
                            "Senha muito curta, digite novamente (No mínimo 8 caracteres)")
                        senha = input("Digite sua senha: ").strip()
                        senha_c = input("Confirme sua senha: ").strip()
                    else:
                        break

                print("Que tipo de usuário você quer criar?")
                print("1 - Básico")
                print("2 - Admin")

                try:
                    opcao = int(input('Sua escolha: '))
                except:
                    print("Digite um valor numérico!")
                    continue

                if opcao == 1:
                    if app.criar_usuario(
                            nome, email, data_nascimento, 'Básico', senha):
                        print("Usuário do tipo Básico criado com sucesso!")

                elif opcao == 2:
                    if app.checa_admin():
                        if app.criar_usuario(
                                nome, email, data_nascimento, 'Admin', senha):
                            print("Usuário do tipo Admin criado com sucesso!")
                    else:
                        print("Não é possível criar mais um Administrador")
                        if app.criar_usuario(
                                nome, email, data_nascimento, 'Básico', senha):
                            print("Usuário do tipo Básico criado com sucesso!")

                else:
                    print("Opção indisponível!")

            elif opcao == 2:
                nome = input("Digite o nome do usuário cadastrado: ").strip()
                senha = input("Digite a senha do usuário: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                novo_nome = input("Digite o novo nome: ").strip()
                novo_email = input("Digite o novo email: ").strip()
                nova_senha = input("Digite a nova senha: ").strip()

                while True:
                    if app.checa_senha(nova_senha):
                        break
                    else:
                        print(
                            "Senha muito curta, digite novamente (No mínimo 8 caracteres)")
                        nova_senha = input("Digite a nova senha: ").strip()

                app.atualizar_usuario(
                    nome, senha, novo_nome, novo_email, nova_senha)

            elif opcao == 3:
                nome = input("Digite o nome do usuário cadastrado: ").strip()
                senha = input("Digite a senha do Usuário: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                app.excluir_usuario(nome)

            elif opcao == 4:
                nome = input("Digite o nome do seu Usuário: ").strip()
                senha = input("Digite a senha do Usuário: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                if app.checa_usuario(nome):
                    app.listar_usuarios()

                else:
                    print("Você não tem permissão para executar isso!")

            elif opcao == 5:
                nome = input("Digite o nome do seu Usuário: ").strip()
                senha = input("Digite a senha do Usuário: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                if app.checa_usuario(nome):
                    print("1 - Buscar por nome;")
                    print("2 - Buscar por email;")
                    opcao = int(input("Sua escolha: "))

                    if opcao == 1:
                        nome = input("Digite o nome do usuário: ").strip()
                        app.buscar_usuarios_nome(nome)

                    elif opcao == 2:
                        email = input("Digite o email do usuário: ").strip()
                        app.buscar_usuarios_email(email)

                else:
                    print("Você não tem permissão para executar isso!")

            else:
                print("Opção indisponível!")

    elif opcao == 2:
        while True:
            print("1 - Criar uma câmera;")
            print("2 - Atualizar uma câmera cadastrada;")
            print("3 - Excluir uma câmera cadastrada;")
            print(
                "4 - Listar as câmeras de um usuário cadastrado(Apenas Administradores);")
            print("5 - Buscar uma câmera cadastrada(Apenas Administradores);")
            print("0 - Voltar")

            try:
                opcao = int(input('Sua escolha: '))
            except:
                print("Digite um valor numérico!")
                continue

            if opcao == 0:
                break
            elif opcao == 1:
                nome = input("Digite o nome da câmera: ").strip()
                nome_usuario = input(
                    "Digite o nome do usário que é dono dessa câmera: ").strip()
                app.criar_camera(nome, nome_usuario)

            elif opcao == 2:
                nome = input("Digite o nome da câmera cadastrada: ").strip()
                senha = input("Digite a senha do dono dessa câmera: ").strip()

                teste = app.seleciona_camera(nome)
                if teste == None:
                    continue

                teste_u = app.seleciona_usuario(teste[1])
                if teste_u[-1] != senha:
                    print("Senha incorreta!")
                    continue

                novo_nome = input("Digite o novo nome: ").strip()
                novo_usuario = input("Digite o novo usuário: ").strip()
                app.atualizar_camera(nome, novo_nome, novo_usuario)

            elif opcao == 3:
                nome = input("Digite o nome da câmera cadastrada: ").strip()
                senha = input("Digite a senha do dono dessa câmera: ").strip()

                teste = app.seleciona_camera(nome)
                if teste == None:
                    print("Câmera não cadastrada!")
                    continue

                teste_u = app.seleciona_usuario(teste[1])
                if teste_u[-1] != senha:
                    print("Senha incorreta!")
                    continue

                app.excluir_camera(nome)

            elif opcao == 4:
                nome = input("Digite o nome do seu Usuário: ").strip()
                senha = input("Digite a sua senha: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                if app.checa_usuario(nome):
                    nome_usuario = input(
                        "Digite o nome do usuário que é dono das câmeras: ").strip()
                    app.listar_cameras_usuario(nome_usuario)

                else:
                    print("Você não tem permissão para executar isso!")

            elif opcao == 5:
                nome = input("Digite o nome do seu Usuário: ").strip()
                senha = input("Digite a sua senha: ").strip()

                teste = app.seleciona_usuario(nome)
                if teste == None:
                    continue
                elif teste[-1] != senha:
                    print("Senha incorreta!")
                    continue

                if app.checa_usuario(nome):
                    nome_camera = input("Digite o nome da câmera: ").strip()
                    app.buscar_cameras(nome_camera)

                else:
                    print("Você não tem permissão para executar isso!")

            else:
                print("Opção indisponível!")
    else:
        print("Opção indisponível!")
