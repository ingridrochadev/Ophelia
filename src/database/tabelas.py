import psycopg2
from os import getenv
from dotenv import load_dotenv
import streamlit as st
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


    def apagar_tabelas(self):
        self.cur.execute('''DROP TABLE IF EXISTS 
                    passageiros, vistos, usuarios, tipos_vistos, voos, historico_embarque''')
        self.conn.commit()
        # print('Tabelas anteriores excluídas.')
        
        
    def criar_tabela_passageiros(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.passageiros
    (
        passaporte character varying(15) NOT NULL,
        nome character varying(150) NOT NULL,
        nacionalidade character varying(5) NOT NULL,
        data_nascimento date NOT NULL,
        PRIMARY KEY (passaporte)
    );  ''')
        self.conn.commit()
        # print('Tabela de passageiros criada.')
        
    # Anotações -> Removi o 'imagem bytea'
    def criar_tabela_vistos(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.vistos
    (
        numero_visto character varying(15) NOT NULL,
        passaporte character varying(15) NOT NULL,
        tipo_visto character varying(10) NOT NULL,
        pais_emitente character varying(15) NOT NULL,
        data_validade date NOT NULL,
        PRIMARY KEY (numero_visto),
        CONSTRAINT fk_passageiro FOREIGN KEY (passaporte)
            REFERENCES public.passageiros (passaporte)                 
    );  ''')
        self.conn.commit()
        # print('Tabela de vistos criada.')
        
    def criar_tabela_usuarios(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.usuarios
    (
        matricula character varying(15) NOT NULL,
        nome character varying(150) NOT NULL,
        email character varying(150) NOT NULL,
        senha character varying(30) NOT NULL,
        cpf character varying(15) NOT NULL,
        PRIMARY KEY (matricula)
    ); ''')
        self.conn.commit()
        # print('Tabela de usuários criada.')
        
        
    def criar_tabela_tipos_vistos(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.tipos_vistos
    (
        tipo character varying(10) NOT NULL,
        regras text NOT NULL,
        PRIMARY KEY (tipo)
    ); ''')
        self.conn.commit()
        # print('Tabela de tipos de vistos criada.')
        
        
    def criar_tabela_voos(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.voos
    (
        numero_voo character varying(15) NOT NULL,
        origem character varying(150) NOT NULL,
        destino character varying(150) NOT NULL,
        data date NOT NULL,    
        horario_previsto time NOT NULL,
        PRIMARY KEY (numero_voo)
    ); ''')
        self.conn.commit()
        # print('Tabela de voos criada.')


    def criar_tabela_historico_embarque(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.historico_embarque
    (   id serial NOT NULL,
        matricula_funcionario character varying(15) NOT NULL,
        passaporte character varying(15) NOT NULL,
        numero_visto character varying(15) NOT NULL,
        numero_voo character varying(15) NOT NULL,
        status character varying(150) NOT NULL,
        data_hora_criacao timestamp with time zone NOT NULL,
        PRIMARY KEY (id),
        CONSTRAINT matricula_funcionario FOREIGN KEY (matricula_funcionario)
            REFERENCES public.usuarios (matricula),
        CONSTRAINT passaporte FOREIGN KEY (passaporte)
            REFERENCES public.passageiros (passaporte),
        CONSTRAINT numero_visto FOREIGN KEY (numero_visto)
            REFERENCES public.vistos (numero_visto),
        CONSTRAINT numero_voo FOREIGN KEY (numero_voo)
            REFERENCES public.voos (numero_voo)
    );
    ''')
        self.conn.commit()
        # print('Tabela de histórico de embarque criada.')
    

    def criar_usuario(self, nome: str, cpf: str, email: str, senha: any, matricula: int):
        if nome and cpf and email and senha and matricula:
            try:
                self.cur.execute("INSERT INTO usuarios (nome, cpf, email, senha, matricula) VALUES (%s, %s, %s, %s, %s)", (nome, cpf, email, senha, matricula))
                self.conn.commit()

            except Exception as error:
                st.error(f"Houve um erro ao inserir usuário. Motivo: {error}")
                self.conn.rollback()
        else:
            st.error("Preencha todos os campos obrigatórios!")
            

    def excluir_usuario(self, matricula: int):
        if matricula:
            try:
                self.cur.execute("DELETE FROM usuarios WHERE matricula = %s", [matricula])
                self.conn.commit()

            except Exception as error:
                st.error(f"Houve um erro ao excluir usuário. Motivo: {error}")
                self.conn.rollback()
        else:
            st.error("Preencha todos os campos obrigatórios!")
            

    # ** Métodos não finalizados / testados
    # -> Criptografia de senha do método 'fazer_login()' será implementado posteriormente
    # -> Ações do método 'fazer_logout()' serão implementadas posteriormente
    def fazer_login(self, email: str, senha: any):
        if email and senha:
            try:
                self.cur.execute("SELECT matricula, nome, email, senha, cpf FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
                login = self.cur.fetchone()
                
                if login:
                    st.success("Login realizado com sucesso! Redirecionando...")
                else:
                    st.error("E-mail e/ou senha incorreta. Tente novamente")
                    
            except Exception as error:
                st.error(f"Ocorreu um erro na tentativa de login. Motivo: {error}")
                
        else:
            st.error("Preencha todos os campos obrigatórios.")
    
    
    def fazer_logout(self):
        pass
        
            
                
if __name__ == '__main__':
    sistema = Sistema()
    sistema.criar_tabela_passageiros()
    sistema.criar_tabela_historico_embarque()
    sistema.criar_tabela_vistos()
    sistema.criar_tabela_tipos_vistos()
    sistema.criar_tabela_voos()
    sistema.criar_tabela_usuarios()