from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def conectar_db():
    try:
        conexao = psycopg2.connect(
            dbname=os.getenv('dbname'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            host=os.getenv('host'),
            port=os.getenv('port')
        )  
        print('Conexão estabelecida com sucesso!')
        return conexao

    except Exception as e:
        print(f'\nOcorreu um erro: {e}')
    return None


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
    conexao = conectar_db()
    cursor = conexao.cursor()
    criar_tabela_passageiros(cursor)
    criar_tabela_vistos(cursor)
    criar_tabela_usuarios(cursor)
    conexao.commit()
    cursor.close()
    conexao.close()