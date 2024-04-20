import psycopg2
from os import getenv
from dotenv import load_dotenv
import bcrypt

load_dotenv()

class Sistema:
    def __init__(self):
        self.conn = self.estabelecer_conexao()
        self.cur = self.conn.cursor()
    
    def estabelecer_conexao(self):
        conn = psycopg2.connect(
            dbname=getenv("DATABASE_NAME"),
            user=getenv("DATABASE_USER"),
            password=getenv("DATABASE_PASSWORD"),
            host=getenv("DATABASE_HOST")
        )
        conn.autocommit = False  # Desativa o modo de autocommit para fazer commits manuais
        return conn
    
    
    def encriptar_senha(self, senha):
        salt = bcrypt.gensalt()
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), salt) # Gera o hash da senha usando o salt
        return salt.decode('utf-8') + hash_senha.decode('utf-8') # Concatena o salt e o hash e retorna str
    
    
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str, matricula: int):
        if nome and cpf and email and senha and matricula:
            try:
                hashed_senha = self.encriptar_senha(senha)
                
                self.cur.execute("INSERT INTO usuarios (nome, cpf, email, senha, matricula) VALUES (%s, %s, %s, %s, %s)", (nome, cpf, email, hashed_senha, matricula))
                self.conn.commit()

            except Exception as error:
                print(f"Houve um erro ao inserir usuário. Motivo: {error}")
                self.conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")
            
            
    def verificar_usuario_cadastrado(self, email, senha):
        try:            
            self.cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email, ))
            senha_str = self.cur.fetchone()[0] # Recebe a senha do banco de dados
            salt = senha_str[:29] # Extrai o salt do hash armazenado
            hash_fornecido = bcrypt.hashpw(senha.encode('utf-8'), salt.encode('utf-8')) # Gera o hash da senha inserida utilizando o mesmo salt
            return senha_str == salt + hash_fornecido.decode('utf-8') # Verifica se o hash gerado corresponde ao hash armazenado
        
        except Exception as e:
            print(f'Ocorreu um erro ao verificar o usuário: {e}')
            # -> Se o email estiver incorreto, está imprimindo essa mensagem
    
    
    def excluir_usuario(self, matricula: int):
        if matricula:
            try:
                self.cur.execute("DELETE FROM usuarios WHERE matricula = %s", [matricula])
                self.conn.commit()

            except Exception as error:
                print(f"Houve um erro ao excluir usuário. Motivo: {error}")
                self.conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")
    
    # ** Métodos não finalizados / testados
    # -> Ações do método 'fazer_logout()' serão implementadas posteriormente
    def fazer_login(self, email: str, senha: str):
        if email and senha:
            try:
                if self.verificar_usuario_cadastrado(email, senha):
                    print("Login realizado com sucesso! Redirecionando...")
                else:
                    print("E-mail e/ou senha incorreta. Tente novamente")
                    
            except Exception as error:
                print(f"Ocorreu um erro na tentativa de login. Motivo: {error}")
                
        else:
            print("Preencha todos os campos obrigatórios.")
    
    def fazer_logout(self):
        pass
