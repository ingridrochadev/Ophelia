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


def apagar_tabelas(cursor):
    cursor.execute('''DROP TABLE IF EXISTS 
                   passageiros, vistos, usuarios, tipos_vistos, voos, historico_embarque''')
    print('Tabelas anteriores excluídas.')

def criar_tabela_passageiros(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.passageiros
(
    passaporte character varying(15) NOT NULL,
    nome character varying(150) NOT NULL,
    nacionalidade character varying(5) NOT NULL,
    data_nascimento date NOT NULL,
    PRIMARY KEY (passaporte)
);  ''')
    print('Tabela de passageiros criada.')


def criar_tabela_vistos(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.vistos
(
    numero_visto character varying(15) NOT NULL,
    passaporte character varying(15) NOT NULL,
    tipo_visto character varying(10) NOT NULL,
    data_validade date NOT NULL,
    entradas character varying(10) NOT NULL,
    anotacoes text,
    imagem bytea,
    PRIMARY KEY (numero_visto),
    CONSTRAINT fk_passageiro FOREIGN KEY (passaporte)
        REFERENCES public.passageiros (passaporte)                 
);  ''')
    
    print('Tabela de vistos criada.')


def criar_tabela_usuarios(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.usuarios
(
    matricula character varying(15) NOT NULL,
    nome character varying(150) NOT NULL,
    email character varying(150) NOT NULL,
    senha character varying(30) NOT NULL,
    cpf character varying(15) NOT NULL,
    PRIMARY KEY (matricula)
); ''')

    print('Tabela de usuários criada.')


def criar_tabela_tipos_vistos(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.tipos_vistos
(
    tipo character varying(10) NOT NULL,
    regras text NOT NULL,
    PRIMARY KEY (tipo)
); ''')
    
    print('Tabela de tipos de vistos criada.')


def criar_tabela_voos(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.voos
(
    numero_voo character varying(15) NOT NULL,
    origem character varying(150) NOT NULL,
    destino character varying(150) NOT NULL,
    data date NOT NULL,    
    horario_previsto time NOT NULL,
    PRIMARY KEY (numero_voo)
); ''')
    
    print('Tabela de voos criada.')


def criar_tabela_historico_embarque(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS public.historico_embarque
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
    
    print('Tabela de histórico de embarque criada.')


if __name__ == '__main__':
    conexao = conectar_db()
    cursor = conexao.cursor()
    apagar_tabelas(cursor)
    criar_tabela_passageiros(cursor)
    criar_tabela_vistos(cursor)
    criar_tabela_usuarios(cursor)
    criar_tabela_tipos_vistos(cursor)
    criar_tabela_voos(cursor)
    criar_tabela_historico_embarque(cursor)
    conexao.commit()
    cursor.close()
    conexao.close()