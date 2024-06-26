from dotenv import load_dotenv
import psycopg2
from os import getenv
import src.database.dependencies as d  #para usar na main
#import dependencies as d  #para rodar sozinho
import datetime as dt


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
    def inserir_dados_ocr_vistos(self, numero_visto, passaporte, tipo_visto, pais_emitente, data_validade, status):
        try:
            self.cur.execute("INSERT INTO vistos (numero_visto, passaporte, tipo_visto, local_emissor, data_validade, status) VALUES (%s, %s, %s, %s, %s, %s)",
                                (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade, status))
            self.conn.commit()
            print("Dados do OCR inseridos na tabela de vistos com sucesso.")
        except Exception as e:
            print(f"Erro ao inserir dados do OCR na tabela de vistos: {e}")
            self.conn.rollback()

    def inserir_dados(self, info_array, status):
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

            self.inserir_dados_ocr_vistos(numero_visto, passaporte, tipo_visto, pais_emitente, data_validade, status)

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

    def editar_dados(self, passaporte, dados):
        nome, nascimento, nacionalidade, tipo_visto, numero_visto, validade, local_emissor, status = dados  # Obtém apenas a data de hoje
        data_nascimento = dt.datetime.strptime(nascimento, "%d-%m-%Y").date()
        data_validade = dt.datetime.strptime(validade, "%d-%m-%Y").date()
        try:
            if nome:
                self.cur.execute("UPDATE public.passageiros SET nome = %s WHERE passaporte = %s", (nome, passaporte))
            if nacionalidade:
                self.cur.execute("UPDATE public.passageiros SET nacionalidade = %s WHERE passaporte = %s", (nacionalidade, passaporte))
            if data_nascimento:
                self.cur.execute("UPDATE public.passageiros SET data_nascimento = %s WHERE passaporte = %s", (data_nascimento, passaporte))
            if numero_visto:
                self.cur.execute("UPDATE public.vistos SET numero_visto = %s WHERE passaporte = %s", (numero_visto, passaporte))
            if tipo_visto:
                self.cur.execute("UPDATE public.vistos SET tipo_visto = %s WHERE passaporte = %s", (tipo_visto, passaporte))
            if local_emissor:
                self.cur.execute("UPDATE public.vistos SET local_emissor = %s WHERE passaporte = %s", (local_emissor, passaporte))
            if data_validade:
                self.cur.execute("UPDATE public.vistos SET data_validade = %s WHERE passaporte = %s", (data_validade, passaporte))
            if status:
                self.cur.execute("UPDATE public.vistos SET status = %s WHERE passaporte = %s", (status, passaporte))
            self.conn.commit()

            return 'Dados alterados com sucesso!'
        
        except Exception as e:
            return f"Erro ao editar dados: {e}"
    
    def listar_vistos_sys(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,
                            vistos.status 
                    FROM vistos 
                    JOIN passageiros ON passageiros.passaporte = vistos.passaporte;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            print(resultados)
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def listar_vistos_asc(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte, 
                            vistos.status
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
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte, 
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            ORDER BY passageiros.nome DESC;'''

            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def listar_vistos_aprovados(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Aprovado';'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados
            
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
            
    def listar_vistos_aprovados_asc(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Aprovado'
            ORDER BY passageiros.nome;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
    def listar_vistos_aprovados_desc(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Aprovado'
            ORDER BY passageiros.nome DESC;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def listar_vistos_negados(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Negado'
            ORDER BY passageiros.nome;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def listar_vistos_negados_asc(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Negado'
            ORDER BY passageiros.nome;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados

        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
    def listar_vistos_negados_desc(self):
        try:
            sql = '''SELECT passageiros.nome,
                            passageiros.passaporte,                            
                            vistos.status
            FROM passageiros 
            JOIN vistos ON passageiros.passaporte = vistos.passaporte
            WHERE vistos.status = 'Negado'
            ORDER BY passageiros.nome DESC;'''
        
            self.cur.execute(sql)
            resultados = self.cur.fetchall()
            return resultados
        
        except Exception as e:
            print(f'Ocorreu um erro: {e}')
    
    def alterar_status_visto(self, passaporte):
        try:
            # Verifica se o passaporte está cadastrado
            self.cur.execute("SELECT status FROM vistos WHERE passaporte = %s", (passaporte, ))
            status = self.cur.fetchone()            
            if status[0] == 'Aprovado':
                self.cur.execute("UPDATE vistos SET status = 'Reprovado' WHERE passaporte = %s", (passaporte, ))
                self.conn.commit()
                print("Status alterado para Reprovado")
            elif status[0] == 'Reprovado':
                self.cur.execute("UPDATE vistos SET status = 'Aprovado' WHERE passaporte = %s", (passaporte, ))
                self.conn.commit()
                print("Status alterado para Aprovado")
            else:
                print("Passaporte não encontrado")    
                
        except Exception as e:
            self.conn.rollback()
            return f'Ocorreu um erro ao alterar o status: {e}'
    
    def imprimir_resultados(self, resultados):
        for resultado in resultados:
            print(resultado)

    def verificar_regras_embarque(self, tipo_visto, dob, expiracao_str, numero_visto):
        dob_date = dt.datetime.strptime(dob, "%d-%m-%Y").date()
        expiracao_date = dt.datetime.strptime(expiracao_str, "%d-%m-%Y").date()
        
        current_date = dt.datetime.now().date()  # Obtém apenas a data de hoje
        
        # Converta dob para datetime
        age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        tipo_encontrado = None  # Defina tipo_encontrado como None inicialmente
        
        self.cur.execute("SELECT numero_visto FROM vistos WHERE numero_visto = %s", (numero_visto, ))
        visto_existe = self.cur.fetchone() 

        if visto_existe:
            return 'O visto informado já existe no banco de dados'

        else:
            # Verifique o tipo de visto
            if tipo_visto:
                self.cur.execute("SELECT tipo, regras FROM tipos_vistos WHERE tipo = %s", (tipo_visto.lower(),))
                tipo_encontrado = self.cur.fetchone()  # Busca apenas um registro

            if tipo_encontrado == None:
                mensagem = 'Tipo de visto inválido'
                return mensagem
            
            else:
                if expiracao_date < current_date: # Verifica se a data de expiração do visto está na validade
                    mensagem = "O visto está vencido!"
                    return mensagem 
                
                if age < 18:  # Verifica se é menor de idade
                    mensagem = "O passageiro é menor de idade. Verificar autorização dos responsáveis."
                    return mensagem
                
                if tipo_encontrado[1]:
                    return tipo_encontrado[1] # Retorna a regra correspondente ao tipo de visto
                else: 
                    mensagem = "Sem regras adicionais"
                    return mensagem

            
    def buscar_por_passaporte(self, passaporte):    
        self.cur.execute("SELECT nome, data_nascimento, nacionalidade FROM public.passageiros WHERE passaporte = %s", (passaporte,))
        dados_passageiro = self.cur.fetchone()  # Retorna a primeira linha encontrada ou None
    
        if dados_passageiro is None:
            return "Passaporte não encontrado no banco de dados"  
    
        self.cur.execute("SELECT tipo_visto, numero_visto, data_validade, local_emissor, status FROM public.vistos WHERE passaporte = %s", (passaporte,))
        dados_vistos = self.cur.fetchall()  
    
        resultado = list(dados_passageiro)
        for visto in dados_vistos:
            resultado.extend(visto)
    
        return resultado 


    def excluir_por_passaporte(self, num_passaporte):
        try:
            #excluir primeiro da tabela de visto pra não ter problema com as FK
            self.cur.execute("DELETE FROM public.vistos WHERE passaporte = %s", (num_passaporte,))
        
            #depois excluir de passageiros
            self.cur.execute("DELETE FROM public.passageiros WHERE passaporte = %s", (num_passaporte,))
        
            self.conn.commit()
        
            return "Dados do passaporte excluídos com sucesso."
    
        except Exception as e:
            self.conn.rollback()
            return "Erro ao excluir dados do passaporte"



if __name__ == '__main__':
            
    funcoes = Funcoes()

    #info_array = leitura_do_passaporte()
    #info_array = ['FERNANDES  STEVE NKLAWRENCE', 'P6966107', '1ND', '1986-01-26', '2017-12-31', 'J1', 'MDR', 'M2728859']
    #funcoes.inserir_dados(info_array)
    
    #tipo = 'c1'.lower()
    #regra = funcoes.verificar_regras_embarque(tipo)
    #print(regra)
      