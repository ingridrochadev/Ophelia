from dotenv import load_dotenv
import psycopg2
from os import getenv
import src.database.dependencies as d
import datetime as dt
#from Versao_Final_OCR import leitura_do_passaporte

load_dotenv()

class Funcoes:
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


    # Método para inserir dados do OCR na tabela de vistos
    def inserir_dados_ocr_passageiros(self, passaporte, nome, nacionalidade, data_nascimento):
        try:
            self.cur.execute("INSERT INTO passageiros (passaporte, nome, nacionalidade, data_nascimento) VALUES (%s, %s, %s, %s)",
                                (passaporte, nome, nacionalidade, data_nascimento))
            self.conn.commit()
            print("Dados do OCR inseridos na tabela de passageiros com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados do OCR na tabela de vistos: {e}")
            self.conn.rollback()


    # Método para inserir dados do OCR na tabela de vistos
    def inserir_dados_ocr_vistos(self, numero_visto, passaporte, tipo_visto, pais_emitente, data_validade):
        try:
            self.cur.execute("INSERT INTO vistos (numero_visto, passaporte, tipo_visto, local_emissor, data_validade) VALUES (%s, %s, %s, %s, %s)",
                                (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade))
            self.conn.commit()
            print("Dados do OCR inseridos na tabela de vistos com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados do OCR na tabela de vistos: {e}")
            self.conn.rollback()


    def inserir_dados(self, info_array):
        try:                       
            nome = info_array[0]
            passaporte = info_array[1]
            nacionalidade = info_array[2]
            data_nascimento = info_array[3]
            data_validade = info_array[4]
            tipo_visto = info_array[5]
            pais_emitente = info_array[6]
            numero_visto = info_array[7]

            # Inserir dados do OCR na tabela 
            self.inserir_dados_ocr_passageiros(passaporte, nome, nacionalidade, data_nascimento)

            self.inserir_dados_ocr_vistos(numero_visto, passaporte, tipo_visto, pais_emitente, data_validade)

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def inserir_status(self, status: str, passaporte):
        try:
            self.cur.execute("UPDATE vistos SET status = %s WHERE passaporte = %s", (status, passaporte))
            self.conn.commit()
            print("Status inserido na tabela de vistos com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir status na tabela de vistos: {e}")
            self.conn.rollback()

    # Tem que alterar para listar o status do embarque
    def listar_vistos(self):
        try:
            sql = '''SELECT passageiros.passaporte, 
                            passageiros.nome,
                            passageiros.nacionalidade,
                            passageiros.data_nascimento,
                            vistos.numero_visto,
                            vistos.tipo_visto,
                            vistos.data_validade
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados
        
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def listar_vistos_asc(self):
        try:
            sql = '''SELECT passageiros.passaporte, 
                            passageiros.nome,
                            passageiros.nacionalidade,
                            passageiros.data_nascimento,
                            vistos.numero_visto,
                            vistos.tipo_visto,
                            vistos.data_validade
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            ORDER BY passageiros.nome;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados
        
        except Exception as e:
            print(f'Ocorreu um erro: {e}')


    def listar_vistos_desc(self):
        try:
            sql = '''SELECT passageiros.passaporte, 
                            passageiros.nome,
                            passageiros.nacionalidade,
                            passageiros.data_nascimento,
                            vistos.numero_visto,
                            vistos.tipo_visto,
                            vistos.data_validade
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            ORDER BY passageiros.nome DESC;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            self.imprimir_resultados(resultados)

        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
    def listar_vistos_sys(self):
        try:
            sql = '''select passageiros.nome, passageiros.passaporte, vistos.status 
                    from vistos, passageiros
                    where passageiros.passaporte = vistos.passaporte;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            # self.imprimir_resultados(resultados)
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')


    def verificar_regras_embarque(self, tipo_visto, dob, expiracao):
        current_date = dt.datetime.now().date()  # Obtém apenas a data de hoje
        dob_date = dt.datetime.combine(dob, dt.datetime.min.time())  # Converte dob para datetime
        age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        tipo_encontrado = None  # Defina tipo_encontrado como None inicialmente
        
        # Verifique o tipo de visto
        self.cur.execute("SELECT regras FROM tipos_vistos WHERE tipo = %s;", (tipo_visto.lower(),))
        tipo_encontrado = self.cur.fetchone()  # Busca apenas um registro
        
        if expiracao < current_date: # Verifica se a data de expiração do visto está na validade
            return "O visto está vencido!"
        
        elif age < 18:
            return "O passageiro é menor de idade. Verificar autorização dos responsáveis." # Verifica se é menor de idade
        
        elif tipo_encontrado:
            return tipo_encontrado # Retorna a regra correspondente ao tipo de visto
        
        else:
            return "Tipo de visto não corresponde a nenhum que conhecemos"

# if __name__ == '__main__':
            
#     funcoes = Funcoes()

    #info_array = leitura_do_passaporte()
    #info_array = ['FERNANDES  STEVE NKLAWRENCE', 'P6966107', '1ND', '1986-01-26', '2017-12-31', 'J1', 'MDR', 'M2728859']
    #funcoes.inserir_dados(info_array)
    
    #tipo = 'c1'.lower()
    #regra = funcoes.verificar_regras_embarque(tipo)
    #print(regra)
    
    # funcoes.listar_vistos_asc()
    #funcoes.listar_vistos_desc()


    #funcoes.cur.close()
    #funcoes.conn.close()
