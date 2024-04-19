from dotenv import load_dotenv
import psycopg2
from os import getenv
import dependencies as d


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


    def extrair_informacoes_txt(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                lines = file.readlines()
            
            nome = lines[0].split(": ")[1].strip()
            passaporte = lines[1].split(": ")[1].strip()
            nacionalidade = lines[2].split(": ")[1].strip()
            data_aniversario = (lines[3].split(": ")[1].strip())
            dia = int(data_aniversario[-2:])
            mes = int(data_aniversario[5:7])
            ano = int(data_aniversario[:4])
            
            data_nascimento = d.date(ano, mes, dia)
            
            sexo = lines[4].split(": ")[1].strip()
            data_validade = (lines[5].split(": ")[1].strip())

            dia = int(data_validade[-2:])
            mes = int(data_validade[5:7])
            ano = int(data_validade[:4])
        
            data_validade = d.date(ano, mes, dia)

            tipo_visto = lines[6].split(": ")[1].strip()
            pais_emitente = lines[7].split(": ")[1].strip()
            numero_visto = lines[8].split(": ")[1].strip()

            # Inserir dados do OCR na tabela 
            self.inserir_dados_ocr_passageiros(passaporte, nome, nacionalidade, data_nascimento)

            self.inserir_dados_ocr_vistos(numero_visto, passaporte, tipo_visto, pais_emitente, data_validade)

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
            self.imprimir_resultados(resultados)

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


    def imprimir_resultados(self, resultados):
        if resultados:
            for visto in resultados:
                print(visto)

    def verificar_regras_embarque(self, tipo_visto):
        self.cur.execute("SELECT regras FROM tipos_vistos WHERE tipo = %s", (tipo_visto,))
        regras = [regra[0] for regra in self.cur.fetchall()]
        for regra in regras:
            if regra:
                return regra
            else:
                return 'Não são necessárias confirmações adicionais.'

        if not regras:
            return 'Tipo de visto não encontrado!'




if __name__ == '__main__':
    
    arquivo = 'src\\database\\informacoes.txt'
    
    funcoes = Funcoes()

    #funcoes.extrair_informacoes_txt(arquivo)    

    #tipo = 'c1'.lower()
    #regra = funcoes.verificar_regras_embarque(tipo)
    #print(regra)
    
    #funcoes.listar_vistos_asc()
    #funcoes.listar_vistos_desc()

    #funcoes.cur.close()
    #funcoes.conn.close()