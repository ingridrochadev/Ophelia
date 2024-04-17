from dotenv import load_dotenv
import psycopg2
from os import getenv
import dependencies as d


load_dotenv()

def conectar_db():
    try:
        conexao = psycopg2.connect(
            dbname=getenv("DATABASE_NAME"),
            user=getenv("DATABASE_USER"),
            password=getenv("DATABASE_PASSWORD"),
            host=getenv("DATABASE_HOST")
        )  
        print('Conexão estabelecida com sucesso!')
        return conexao

    except Exception as e:
        print(f'\nOcorreu um erro: {e}')
    return None


# Método para inserir dados do OCR na tabela de vistos
def inserir_dados_ocr_passageiros(passaporte, nome, nacionalidade, data_nascimento, cursor):
    try:
        cursor.execute("INSERT INTO passageiros (passaporte, nome, nacionalidade, data_nascimento) VALUES (%s, %s, %s, %s)",
                             (passaporte, nome, nacionalidade, data_nascimento))
        #self.conn.commit()
        print("Dados do OCR inseridos na tabela de passageiros com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados do OCR na tabela de vistos: {e}")
        #self.conn.rollback()


# Método para inserir dados do OCR na tabela de vistos
def inserir_dados_ocr_vistos(numero_visto, passaporte, tipo_visto, pais_emitente, data_validade, cursor):
    try:
        cursor.execute("INSERT INTO vistos (numero_visto, passaporte, tipo_visto, local_emissor, data_validade) VALUES (%s, %s, %s, %s, %s)",
                             (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade))
        #self.conn.commit()
        print("Dados do OCR inseridos na tabela de vistos com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir dados do OCR na tabela de vistos: {e}")
        #self.conn.rollback()


def extrair_informacoes_txt(arquivo, cursor):
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
    inserir_dados_ocr_passageiros(passaporte, nome, nacionalidade, data_nascimento, cursor)
    conexao.commit()

    inserir_dados_ocr_vistos(numero_visto, passaporte, tipo_visto, pais_emitente, data_validade, cursor)
    conexao.commit()



if __name__ == '__main__':
    
    arquivo = 'Ophelia\\src\\database\\informacoes.txt'
    
    conexao = conectar_db()
    cursor = conexao.cursor()

    extrair_informacoes_txt(arquivo, cursor)    

    cursor.close()
    conexao.close()