from dotenv import load_dotenv
import psycopg2
from os import getenv

load_dotenv()

class Criar_bd:
    def __init__(self):
        self.estabelecer_conexao()             
        self.cur = self.conn.cursor()

    def estabelecer_conexao(self):
        try:
            self.conn = psycopg2.connect(
                dbname=getenv("DATABASE_NAME"),
                user=getenv("DATABASE_USER"),
                password=getenv("DATABASE_PASSWORD"),
                host=getenv("DATABASE_HOST")
            )  
            self.conn.autocommit = False  # Desativa o modo de autocommit para fazer commits manuais

            print('Conexão estabelecida com sucesso!')
            
            
        except Exception as e:
            print(f'\nOcorreu um erro ao conectar ao banco de dados: {e}')


    def apagar_tabelas(self):
        self.cur.execute('''DROP TABLE IF EXISTS 
                    passageiros, vistos, usuarios, tipos_vistos, voos, historico_embarque''')
        print('Tabelas anteriores excluídas.')


    def criar_tabela_passageiros(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.passageiros
    (
        passaporte character varying(15) NOT NULL,
        nome character varying(150) NOT NULL,
        nacionalidade character varying(5) NOT NULL,
        data_nascimento date NOT NULL,
        PRIMARY KEY (passaporte)
    );  ''')
        print('Tabela de passageiros criada.')


    def criar_tabela_vistos(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.vistos
    (
        numero_visto character varying(15) NOT NULL,
        passaporte character varying(15) NOT NULL,
        tipo_visto character varying(10) NOT NULL,
        local_emissor character varying(15) NOT NULL,
        data_validade date NOT NULL,
        PRIMARY KEY (numero_visto),
        CONSTRAINT fk_passageiro FOREIGN KEY (passaporte)
            REFERENCES public.passageiros (passaporte)                 
    );  ''')
        
        print('Tabela de vistos criada.')


    def criar_tabela_usuarios(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.usuarios
    (
        matricula character varying(15) NOT NULL,
        nome character varying(150) NOT NULL,
        email character varying(150) NOT NULL,
        senha character varying(150) NOT NULL,
        cpf character varying(15) NOT NULL,
        tipo_usuario character varying(15) NOT NULL,
        PRIMARY KEY (matricula)
    ); ''')

        print('Tabela de usuários criada.')


    def criar_tabela_tipos_vistos(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS public.tipos_vistos
    (
        tipo character varying(10) NOT NULL,
        descricao text NOT NULL,
        regras text,
        PRIMARY KEY (tipo)
    ); ''')
        
        print('Tabela de tipos de vistos criada.')


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
        
        print('Tabela de voos criada.')


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
        
        print('Tabela de histórico de embarque criada.')


    def inserir_dados_passageiros(self):
        self.cur.execute('''INSERT INTO public.passageiros (passaporte, nome, nacionalidade, data_nascimento)
    VALUES 
    ('ABC123456', 'John Smith', 'USA', '1981-06-10'),
    ('DEF234567', 'Emma Johnson', 'CAN', '1979-03-22'),
    ('GHI345678', 'Michael Williams', 'GBR', '1992-09-05'),
    ('JKL456789', 'Sophia Brown', 'AUS', '1987-11-18'),
    ('MNO567890', 'Daniel Jones', 'GER', '1980-02-27'),
    ('PQR678901', 'Olivia Davis', 'FRA', '1975-07-15'),
    ('STU789012', 'William Miller', 'BRA', '1990-04-30'),
    ('VWX890123', 'Emily Wilson', 'IND', '1985-12-12'),
    ('YZA901234', 'Matthew Moore', 'CHN', '1968-08-25'),
    ('BCD012345', 'Isabella Taylor', 'JPN', '1983-10-03'),
    ('EFG123456', 'David Brown', 'USA', '1995-02-28'),
    ('HIJ234567', 'Sophie Martinez', 'ESP', '1988-05-17'),
    ('KLM345678', 'Andrew Johnson', 'CAN', '1991-09-11'),
    ('NOP456789', 'Jessica Lee', 'KOR', '1977-12-09'),
    ('QRS567890', 'Ryan Chen', 'TWN', '1984-03-24');
    ''')
        print('Dados de passageiros inseridos')
    
    def inserir_dados_vistos(self):
        self.cur.execute('''INSERT INTO public.vistos (numero_visto, passaporte, tipo_visto, local_emissor, data_validade)
    VALUES 
    ('V1B123456', 'ABC123456', 'B1', 'USA', '2034-01-23'),
    ('V2B234567', 'DEF234567', 'B2', 'CAN','2033-12-15'),
    ('V3C345678', 'GHI345678', 'C1', 'GBR', '2033-11-20'),
    ('V4D456789', 'JKL456789', 'D', 'AUS','2033-10-05'),
    ('V5F567890', 'MNO567890', 'F1', 'GER', '2033-09-10'),
    ('V6H678901', 'PQR678901', 'H1B', 'FRA', '2033-08-25'),
    ('V7K789012', 'STU789012', 'K1', 'BRA', '2033-07-30'),
    ('V8J890123', 'VWX890123', 'J1', 'IND', '2033-06-15'),
    ('V9L901234', 'YZA901234', 'L1', 'CHN', '2033-05-20'),
    ('V10M012345', 'BCD012345', 'M', 'JPN', '2033-04-05'),
    ('V11O123456', 'EFG123456', 'O1', 'USA', '2034-01-23'),
    ('V12P234567', 'HIJ234567', 'P1', 'ESP', '2033-12-15'),
    ('V13R345678', 'KLM345678', 'R1', 'CAN', '2033-11-20'),
    ('V14TN456789', 'NOP456789', 'TN', 'KOR', '2033-10-05'),
    ('V15B567890', 'QRS567890', 'B1', 'TWN', '2033-09-10');
    ''')
        print('Dados de passageiros inseridos')


    def inserir_tipos_vistos(self):
        self.cur.execute('''INSERT INTO public.tipos_vistos (tipo, descricao, regras) VALUES
    ('b1', 'Visto de embarque para turismo, visitas a amigos ou parentes, tratamento médico, etc.', 'Para o tipo B1, verificar se o empregado doméstico está acompanhado do seu empregador.'),
    ('b2', 'Visto de embarque para turismo, visitas a amigos ou parentes, tratamento médico, etc.', NULL),
    ('b3', 'Visto de embarque para turismo, visitas a amigos ou parentes, tratamento médico, etc.', NULL),
    ('c1', 'Visto de trânsito.', 'Verificar se o destino final do passageiro é fora dos EUA.'),
    ('f1', 'Visto de embarque para estudantes matriculados em instituições acadêmicas ou estudantes não acadêmicos. Limitado a instituições educacionais específicas.', 'Verificar o documento de Formulário I-20 da instituição educacional.'),
    ('m1', 'Visto de embarque para estudantes matriculados em instituições acadêmicas ou estudantes não acadêmicos. Limitado a instituições educacionais específicas.', 'Verificar o documento de Formulário I-20 da instituição educacional.'),
    ('m', 'Visto de embarque para estudantes matriculados em instituições acadêmicas ou estudantes não acadêmicos. Limitado a instituições educacionais específicas.', 'Verificar o documento de Formulário I-20 da instituição educacional.'),
    ('j1', 'Visto de embarque para participantes de programas de intercâmbio.', 'Verificar o documento: carta do programa de intercâmbio.'),
    ('h1b', 'Visto de embarque para profissionais estrangeiros em ocupações especializadas.', 'Verificar o documento de contrato de trabalho ou oferta de emprego válida.'),
    ('l1', 'Visto de embarque para funcionários de empresas multinacionais transferidos.', 'Verificar o documento: carta de transferência da empresa multinacional.'),
    ('o1', 'Visto de embarque para pessoas com habilidades extraordinárias ou realizações notáveis.', 'Verificar o documento de comprovante de habilidades extraordinárias.'),
    ('e1', 'Visto de embarque para comerciantes de países com tratados de comércio.', 'Verificar o documento: provas de comércio.'),
    ('e2', 'Visto de embarque para investidores de países com tratados de comércio.', 'Verificar o documento: provas de investimento.'),
    ('k1', 'Visto de embarque para noivos ou noivas de cidadãos americanos para casar em 90 dias.', 'Verificar o documento: processo de casamento.'),
    ('a1', 'Visto de embarque para diplomatas e funcionários de governos estrangeiros.', 'Verificar o documento: diploma diplomático.'),
    ('a2', 'Visto de embarque para diplomatas e funcionários de governos estrangeiros.', 'Verificar o documento: diploma diplomático.'),
    ('g1', 'Visto de embarque para funcionários de organizações internacionais.', 'Verificar o documento: carta da organização internacional.'),
    ('g2', 'Visto de embarque para funcionários de organizações internacionais.', 'Verificar o documento: carta da organização internacional.'),
    ('g3', 'Visto de embarque para funcionários de organizações internacionais.', 'Verificar o documento: carta da organização internacional.'),
    ('g4', 'Visto de embarque para funcionários de organizações internacionais.', 'Verificar o documento: carta da organização internacional.'),
    ('g5', 'Visto de embarque para funcionários de organizações internacionais.', 'Verificar o documento: carta da organização internacional.'),
    ('r1', 'Visto de embarque para trabalhadores religiosos.', 'Verificar o documento: provas de afiliação religiosa.'),
    ('t', 'Visto de embarque para vítimas de tráfico humano.', 'Verificar o documento: provas de vítima de tráfico humano.'),
    ('to', 'Visto de embarque para vítimas de tráfico humano.', 'Verificar o documento: provas de vítima de tráfico humano.'),
    ('u', 'Visto de embarque para vítimas de crimes.', 'Verificar o documento: provas de vítima de crime.'),
    ('v', 'Visto de embarque para cônjuges ou filhos de residentes legais permanentes.', 'Verificar o documento: provas de relacionamento.'),
    ('d', 'Visto de embarque para tripulantes de navios ou aeronaves.', 'Verificar o documento de licença de tripulação.'),
    ('nato', 'Visto de embarque para membros da OTAN e suas famílias.', 'Verificar o documento de identificação da OTAN.'),
    ('p1', 'Visto de atleta/artista de destaque.', 'Verificar documentação que comprove o status de atleta ou artista de destaque.'),
    ('tn', 'Visto do Acordo de Livre Comércio da América do Norte (NAFTA).', NULL);
    ''')


    def criar_tabelas(self):
        self.criar_tabela_passageiros()
        self.criar_tabela_vistos()
        self.criar_tabela_usuarios()
        self.criar_tabela_tipos_vistos()
        self.criar_tabela_voos()
        self.criar_tabela_historico_embarque()
        self.conn.commit()

    def inserir_dados(self):
        self.inserir_dados_passageiros()
        self.inserir_dados_vistos()
        self.inserir_tipos_vistos()
        self.conn.commit()
    
    def criar_usuario(self, nome, cpf, email, senha, matricula, tipo_usuario):
        try:
            self.cur.execute("INSERT INTO usuarios (matricula, nome, email, senha, cpf, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)",
                             (matricula, nome, email, senha, cpf, tipo_usuario))
            print("Usuário criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")

# Restante do código...

if __name__ == '__main__':
    bd = Criar_bd()

    bd.apagar_tabelas()
    bd.criar_tabelas()
    bd.inserir_dados()

    # Inserindo os usuários
    bd.criar_usuario("Administrador", "12345678900", "admin@email.com", "admin", "ADM001", "administrador")
    bd.criar_usuario("Usuário Normal", "98765432100", "user@email.com", "user", "USR001", "user")
        
    bd.cur.close()
    bd.conn.close()



# if __name__ == '__main__':
#     bd = Criar_bd()

#     bd.apagar_tabelas()
#     bd.criar_tabelas()
#     bd.inserir_dados()
    
        
#     bd.cur.close()
#     bd.conn.close()