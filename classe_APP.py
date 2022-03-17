import psycopg2
from datetime import datetime


class Aplicativo:
    def __init__(self):
        self.conexao = psycopg2.connect(
            host="localhost",
            database="desafio",
            user="postgres",
            password="112505"
        )
        self.cursor = self.conexao.cursor()

    # Funções da tabela de Usuários:
    def criar_usuario(self, nome, email, data_nascimento, tipo, senha):
        try:
            consulta = 'INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s, %s)'
            self.cursor.execute(consulta, (nome, email, data_nascimento, tipo,
                                           datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d'), senha))
        except:
            print("Nome e/ou email indisponível/indisponíveis!")
            return False

        self.conexao.commit()
        return True

    def excluir_usuario(self, nome):
        consulta = 'DELETE FROM usuarios WHERE nome = %s'
        self.cursor.execute(consulta, (nome,))

        print("Usuário excluído")
        self.conexao.commit()

    def atualizar_usuario(self, nome, senha, novo_nome, email, nova_senha):
        try:
            consulta = 'UPDATE usuarios SET nome = %s, email = %s, data_atualizacao=%s, senha = %s WHERE nome = %s AND senha = %s'
            self.cursor.execute(consulta, (novo_nome, email, str(
                datetime.today().strftime("%Y-%m-%d")), nova_senha, nome, senha))
        except:
            print("Nome e/ou email indisponível/indisponíveis!")
            return

        print("Usuário atualizado!")
        self.conexao.commit()

    def listar_usuarios(self):
        self.cursor.execute('SELECT * FROM usuarios')

        count = 1
        for linha in self.cursor.fetchall():
            print(f'Usuário {count}')
            print(
                f'  Nome: {linha[0]} \n  Email:{linha[1]} \n  Data de nascimento: {linha[2]} \n  Tipo do usuário: {linha[3]}')
            print()
            count += 1

    def buscar_usuarios_nome(self, nome):
        consulta = 'SELECT * FROM usuarios WHERE nome LIKE %s'
        self.cursor.execute(consulta, (f'%{nome}%',))

        for linha in self.cursor.fetchall():
            print(
                f'  Nome: {linha[0]} \n  Email:{linha[1]} \n  Data de nascimento: {linha[2]} \n  Tipo do usuário: {linha[3]}')
            print()

    def buscar_usuarios_email(self, email):
        consulta = 'SELECT * FROM usuarios WHERE email = %s'
        self.cursor.execute(consulta, (email,))

        for linha in self.cursor.fetchall():
            print(
                f'  Nome: {linha[0]} \n  Email:{linha[1]} \n  Data de nascimento: {linha[2]} \n  Tipo do usuário: {linha[3]}')
            print()

    def seleciona_usuario(self, nome):
        consulta = 'SELECT * FROM usuarios WHERE nome = %s'
        self.cursor.execute(consulta, (nome,))

        try:
            lista = self.cursor.fetchall()[0]
        except:
            print("Usuário não cadastrado")
            return

        return lista

    # Funções da tabela de Câmeras:
    def criar_camera(self, nome, nome_usuario):
        try:
            consulta = 'INSERT INTO cameras VALUES (%s, %s, %s, %s)'
            self.cursor.execute(consulta, (nome, nome_usuario,
                                           str(datetime.today().strftime(
                                               "%Y-%m-%d")),
                                           str(datetime.today().strftime("%Y-%m-%d"))))
        except psycopg2.errors.UniqueViolation:
            print("Nome indisponível!")
            return
        except psycopg2.errors.ForeignKeyViolation:
            print("Usuário não cadastrado!")
            return

        print("Câmera adicionada com sucesso!")
        self.conexao.commit()

    def excluir_camera(self, nome):
        consulta = 'DELETE FROM cameras WHERE nome = %s'
        self.cursor.execute(consulta, (nome,))

        print("Câmera excluída!")
        self.conexao.commit()

    def atualizar_camera(self, nome, novo_nome, novo_usuario):
        try:
            consulta = 'UPDATE cameras SET nome = %s, nome_usuario = %s, data_atualizacao = %s WHERE nome = %s'
            self.cursor.execute(
                consulta, (novo_nome, novo_usuario, datetime.today().strftime('%Y-%m-%d'), nome))
        except psycopg2.errors.UniqueViolation:
            print("Nome indisponível!")
            return
        except psycopg2.errors.ForeignKeyViolation:
            print("Câmera não cadastrada!")
            return

        print("Câmera atualizada!")
        self.conexao.commit()

    def listar_cameras_usuario(self, nome_usuario):
        self.cursor.execute(
            "SELECT * FROM cameras WHERE nome_usuario = %s", (nome_usuario, ))

        print(f'Camêras do usuário: {nome_usuario}')
        for linha in self.cursor.fetchall():
            print(f'  -{linha[0]}')

        print()

    def buscar_cameras(self, nome):
        consulta = 'SELECT * FROM cameras WHERE nome = %s'
        self.cursor.execute(consulta, (nome,))

        for linha in self.cursor.fetchall():
            print(f'  Nome da câmera: {linha[0]}\n  Nome do dono: {linha[1]}')

    def seleciona_camera(self, nome):
        consulta = 'SELECT * FROM cameras WHERE nome = %s'
        self.cursor.execute(consulta, (nome,))

        try:
            lista = self.cursor.fetchall()[0]
        except:
            print("Usuário não cadastrado")
            return

        return lista

    # Funções auxiliares
    def checa_usuario(self, nome):
        consulta = "SELECT * FROM public.usuarios WHERE nome = %s"
        self.cursor.execute(consulta, (nome,))

        try:
            teste = self.cursor.fetchall()[0]
        except:
            print("Ocorreu algum erro! Tente Novamente")
            return

        if teste[3] == 'Admin':
            return True
        else:
            return False

    def checa_senha(self, senha):
        if len(senha) < 8:
            return False
        else:
            return True

    def checa_admin(self):
        consulta = "SELECT COUNT(nome) from public.usuarios WHERE tipo = 'Admin';"
        self.cursor.execute(consulta)
        try:
            retorno = self.cursor.fetchall()[0]
        except:
            print("Ocorreu algum erro!")

        if retorno[0] == 0:
            return True
        else:
            return False

    def fechar(self):
        self.cursor.close()
        self.conexao.close()
