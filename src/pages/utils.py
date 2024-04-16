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
    
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str, matricula: int):
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
    def fazer_login(self, email: str, senha: str):
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
