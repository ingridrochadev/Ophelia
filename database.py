import psycopg2
from os import getenv
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

class Sistema:
    def estabelecer_conexao(self):
        conn = psycopg2.connect(
            dbname=getenv("DATABASE_NAME"),
            user=getenv("DATABASE_USER"),
            password=getenv("DATABASE_PASSWORD"),
            host=getenv("DATABASE_HOST")
        )
        conn.autocommit = False  # Desativa o modo de autocommit para fazer commits manuais
        return conn

    def criar_usuario(self, conn, nome: str, cpf: str, email: str, senha: any, matricula: int):
        if conn and nome and cpf and email and senha and matricula:
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usuarios (nome, cpf, email, senha, matricula) VALUES (%s, %s, %s, %s, %s)", (nome, cpf, email, senha, matricula))
                conn.commit()
                # print(f"Usuário '{oame}' inserido com sucesso!") -> Perguntar pro grupo depois
                cur.close()

            except Exception as error:
                print(f"Houve um erro ao inserir usuário. Motivo: {error}")
                conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")
            

    def excluir_usuario(self, conn, matricula: int):
        if conn and matricula:
            try:
                cur = conn.cursor()
                cur.execute("DELETE FROM usuarios WHERE matricula = %s", [matricula])
                conn.commit()
                # print(f"Usuário '{nome}' excluído com sucesso!") -> Perguntar pro grupo depois
                cur.close()

            except Exception as error:
                print(f"Houve um erro ao excluir usuário. Motivo: {error}")
                conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")
            
    def gerar_id(self, conn):
        try:
            id_passageiro_str = str(uuid4())
            id_passageiro_int = int(''.join(c for c in id_passageiro_str[:6] if c.isdigit()))
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM passageiros WHERE id = %s", (int(id_passageiro_int),))
            count = cur.fetchone()[0]
            if count == 0:
                conn.commit()
                cur.close()
                return id_passageiro_int
            else:
                print("ID já existe na tabela")
                return None
                   
        except Exception as error:
                print(f"Houve um erro ao gerar ID. Motivo: {error}")
                conn.rollback()
            

class Funcionario:
    def criar_novo_visto(self, conn, nome: str, num_documento: str, nacionalidade: str, data_nascimento: str, numero_visto: int, passaporte: int, tipo_visto: str, numero_controle: str, data_emissao: str, data_validade: str, entradas: str, anotacoes: str):
        if nome and num_documento and nacionalidade and data_nascimento and numero_visto and passaporte and tipo_visto and numero_controle and data_emissao and data_validade and entradas and anotacoes:
            try:
                cur = conn.cursor()
                id_passageiro = sistema.gerar_id(conn)
                cur.execute("INSERT INTO passageiros (id, nome, documento, nacionalidade, data_nascimento) VALUES (%s, %s, %s, %s, %s)", (id_passageiro, nome, num_documento, nacionalidade, data_nascimento))
                cur.execute("INSERT INTO vistos (numero_visto, id_passageiro, passaporte, tipo_visto, numero_controle, data_emissao, data_validade, entradas, anotacoes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (numero_visto, id_passageiro, passaporte, tipo_visto, numero_controle, data_emissao, data_validade, entradas, anotacoes))
                conn.commit()
                # print(f"Passageiro '{nome}' e visto '{numero_visto}' inserido com sucesso!") -> Perguntar pro grupo depois
                cur.close()

            except Exception as error:
                print(f"Houve um erro ao validar o visto. Motivo: {error}")
                conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")



#
def editar_usuario(conn, criteria_column, criteria_value, new_id, new_name, new_salary, new_date):
    try:
        cur = conn.cursor()
        cur.execute("UPDATE funcionarios SET id = %s, nome = %s, salario = %s, data_contratacao = %s WHERE {} = %s".format(criteria_column), (new_id, new_name, new_salary, new_date, criteria_value))
        conn.commit()
        print(f"Usuário '{new_name}' atualizado com sucesso!")
        cur.close()

    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")
        conn.rollback()

if __name__ == "__main__":
    sistema = Sistema()
    funcionario = Funcionario()
    conn = sistema.estabelecer_conexao()
    
    sistema.criar_usuario(conn, "Yasmim Ferreira dos Santos", "123.456.789-01", "yasmim@alphaedtech.com", "yasmim123", 124031731)
    # sistema.excluir_usuario(conn, 124031731)

    funcionario.criar_novo_visto(conn, "Jose Antonio Sanchez Mejia", "123.456.789-01", "D", "20NOV1967", 6044378, 2347472, "B-1", "20010798250078", "25MAR2002", "19MAR2012", "M", "-")

    # Exemplo de atua]lização
    # update_user(conn, "nome", "Zanetti", 101, "Luis Gustavo Zanetti", 6700, "2021-07-16")

    conn.close()