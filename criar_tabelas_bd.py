from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()

def estabelecer_conexao():
        conn = psycopg2.connect(
            dbname=getenv("DATABASE_NAME"),
            user=getenv("DATABASE_USER"),
            password=getenv("DATABASE_PASSWORD"),
            host=getenv("DATABASE_HOST")
        )
        conn.autocommit = False  # Desativa o modo de autocommit para fazer commits manuais
        return conn


def criar_tabela_passageiros(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.passageiros
(
    id serial NOT NULL,
    nome character varying(150) NOT NULL,
    documento character varying(15) NOT NULL,
    nacionalidade character(3) NOT NULL,
    data_nascimento date NOT NULL,
    PRIMARY KEY (id)
);  ''')


def criar_tabela_vistos(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.vistos
(
    numero_visto integer NOT NULL,
    id_passageiro integer NOT NULL,
    passaporte integer NOT NULL,
    tipo_visto character varying(10) NOT NULL,
    numero_controle integer,
    data_emissao date NOT NULL,
    data_validade date NOT NULL,
    entradas character varying(10) NOT NULL,
    anotacoes text,
    PRIMARY KEY (numero_visto),
    CONSTRAINT fk_passageiro FOREIGN KEY (id_passageiro)
        REFERENCES public.passageiros (id)                 
);  ''')



def criar_tabela_usuarios(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.usuarios
(
    matricula integer NOT NULL,
    nome character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    senha character varying(30) NOT NULL,
    cpf character varying(15) NOT NULL,
    PRIMARY KEY (matricula)
); ''')


if __name__ == '__main__':
    conexao = estabelecer_conexao()
    cursor = conexao.cursor()
    criar_tabela_passageiros(cursor)
    criar_tabela_vistos(cursor)
    criar_tabela_usuarios(cursor)
    conexao.commit()
    cursor.close()
    conexao.close()