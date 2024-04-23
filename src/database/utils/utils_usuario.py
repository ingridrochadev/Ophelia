import psycopg2
from os import getenv
from dotenv import load_dotenv
import bcrypt
import re

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
    
    
    def encriptar_senha(self, senha):
        salt = bcrypt.gensalt()
        hash_senha = bcrypt.hashpw(senha.encode('utf-8'), salt) # Gera o hash da senha usando o salt
        return salt.decode('utf-8') + hash_senha.decode('utf-8') # Concatena o salt e o hash e retorna str
    
    
    def validar_cpf(self, cpf: str):
        if len(cpf) == 11 and cpf.isdigit():
            # Verifica se todos os dígitos são iguais
            if len(set(cpf)) == 1:
                print("CPF inválido! Tente novamente.")
                return False
                
            # * Verificação do 1° dígito:
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9)) 
            verificador1 = (soma * 10) % 11
            
            # * Verificação do 2° dígito:
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            verificador2 = (soma * 10) % 11
            
            if verificador1 == int(cpf[9]) and verificador2 == int(cpf[10]):
                print("CPF válido!")
                return True
            else:
                print("CPF inválido! Tente novamente.")
                return False
        else:
            print("CPF inválido! Tente novamente.")
            return False
        
    
    def validar_email(self, email: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            print("E-mail válido!")
            return True
        else:
            print("O e-mail não é válido!")
            return False
            
            
    def validar_senha(self, senha: str):
        requisitos = {
            "min_numero": 1,
            "min_maiuscula": 1,
            "min_minuscula": 1,
            "min_simbolo": 1,
            "min_tamanho": 6
        }
        # Verifica os requisitos mínimos para a senha
        if (len(senha) < requisitos["min_tamanho"] or
            len(re.findall(r"[A-Z]", senha)) < requisitos["min_maiuscula"] or
            len(re.findall(r"[a-z]", senha)) < requisitos["min_minuscula"] or
            len(re.findall(r"[0-9]", senha)) < requisitos["min_numero"] or
            len(re.findall(r"[@#$]", senha)) < requisitos["min_simbolo"]):
            
            print("Senha inválida! A senha deve conter letras minúsculas, maiúsculas, números e símbolos e ter no minimo 8 caracteres.")
            return False
        else:
            print("Senha válida")
            return True
    
    
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str, matricula: str, tipo_usuario: str):
        if nome and cpf and email and senha and matricula and tipo_usuario:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                hashed_senha = self.encriptar_senha(senha)
                
                if self.validar_cpf(cpf) and self.validar_email(email) and self.validar_senha(senha):
                    cur.execute("INSERT INTO usuarios (nome, cpf, email, senha, matricula, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)", 
                                (nome, cpf, email, hashed_senha, matricula, tipo_usuario))
                    conn.commit()
                else:
                    print("Os dados informados não são válidos! Tente novamente.")

            except Exception as error:
                print(f"Houve um erro ao inserir usuário. Motivo: {error}")
                conn.rollback()
                
            finally:
                cur.close()
                conn.close()
        else:
            print("Preencha todos os campos obrigatórios!")
        
        
    def excluir_usuario(self, matricula: str):
        if matricula:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                cur.execute("DELETE FROM usuarios WHERE matricula = %s", [matricula])
                conn.commit()

            except Exception as error:
                print(f"Houve um erro ao excluir usuário. Motivo: {error}")
                conn.rollback()
                
            finally:
                cur.close()
                conn.close()
        else:
            print("Preencha todos os campos obrigatórios!")
    
    
    def fazer_login(self, email: str, senha: str):
        if email and senha:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                # Verifica se o email está cadastrado
                cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email, ))
                usuario = cur.fetchone()
                if usuario:
                    senha_str = usuario[0] # Recebe a senha do banco de dados
                    salt = senha_str[:29] # Extrai o salt do hash armazenado
                    hash_fornecido = bcrypt.hashpw(senha.encode('utf-8'), salt.encode('utf-8')) # Gera o hash da senha inserida utilizando o mesmo salt
                    
                    # Verifica se o hash gerado corresponde ao hash armazenado
                    if senha_str == salt + hash_fornecido.decode('utf-8'):
                        print("Login realizado com sucesso! Redirecionando...")
                        return True
                    else: 
                        print("E-mail e/ou senha incorreta. Tente novamente!")
                        return False
                else:
                    return False
                    
            except Exception as error:
                print(f"Ocorreu um erro na tentativa de login. Motivo: {error}")
                return False
            
            finally:
                cur.close()
                conn.close()
                
        else:
            print("Preencha todos os campos obrigatórios.")
            return False
    
    def verificar_tipo_perfil(self, email):
        if email:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                cur.execute("SELECT tipo_usuario FROM usuarios WHERE email = %s", (email, ))
                perfil = cur.fetchone()
                if perfil[0] == "Administrador":
                    return 'admin'
                elif perfil[0] == "Usuário":
                    return 'user'
                else:
                    pass
                    
            except Exception as error:
                print(f"Ocorreu um erro na tentativa de login. Motivo: {error}")
                return "Sem Acesso"
            
            finally:
                cur.close()
                conn.close()
                
        else:
            return "Preencha todos os campos obrigatórios."
            
    def alterar_senha(self, email: str, senha_armazenada: str, nova_senha: str, nova_senha2: str):
        if email and senha_armazenada and nova_senha and nova_senha2:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                # Verifica se o email está cadastrado
                cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email, ))
                usuario = cur.fetchone()
                if usuario:
                    senha_str = usuario[0] # Recebe a senha do banco de dados
                    salt = senha_str[:29] # Extrai o salt do hash armazenado
                    hash_fornecido = bcrypt.hashpw(senha_armazenada.encode('utf-8'), salt.encode('utf-8')) # Gera o hash da senha inserida utilizando o mesmo salt
                    
                    # Verifica se o hash gerado corresponde ao hash armazenado
                    if senha_str == salt + hash_fornecido.decode('utf-8'):
                        if nova_senha == nova_senha2:
                            # Senhas correspondem, parte pra alteração
                            hashed_senha = self.encriptar_senha(nova_senha)
                            cur.execute("UPDATE usuarios SET senha = %s WHERE email = %s", (hashed_senha, email))
                            conn.commit()
                            return "Verificado"
                        else:
                            return "As senhas não correspondem. Tente novamente!"
                            
                    else: 
                        return "E-mail e/ou senha incorreta. Tente novamente!"
                        
                else:
                    return "E-mail e/ou senha incorreta. Tente novamente!"
                
            except Exception as error:
                conn.rollback()
                return f'Ocorreu um erro ao alterar a senha: {error}'
                
            finally:
                cur.close()
                conn.close()
        else:
            return "Preencha todos os campos obrigatórios!"
            
            
    def redefinir_senha(self, email, nova_senha, nova_senha2):
        if email and nova_senha and nova_senha2:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                # Verifica se o email está cadastrado
                cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email, ))
                usuario = cur.fetchone()
                if usuario:
                    if nova_senha == nova_senha2:
                        # Senhas correspondem, parte pra alteração
                        hashed_senha = self.encriptar_senha(self, nova_senha)
                        self.cur.execute("UPDATE usuarios SET senha = %s WHERE email = %s", (hashed_senha, email))
                        self.conn.commit()
                        print("Senha alterada com sucesso!")
                    else:
                        print("As senhas não correspondem. Tente novamente!")
                            
                else: 
                    print("E-mail e/ou senha incorreta. Tente novamente!")
                
            except Exception as error:
                print(f'Ocorreu um erro ao redefinir a senha: {error}')
                self.conn.rollback()
                
            finally:
                self.cur.close()
                self.conn.close()
        else:
            print("Preencha todos os campos obrigatórios!")

class Funcionario:
    def __init__(self):
        self.sistema = Sistema()
        self.conn = self.sistema.estabelecer_conexao()
        self.cur = self.conn.cursor()
    
    # ** Métodos não finalizados / testados
    def editar_usuario(self, matricula: str, novo_email: None, nova_senha: None):
        if matricula:
            try:
                if novo_email:
                    self.cur.execute("UPDATE usuarios SET email = %s WHERE matricula = %s", (novo_email, matricula))
                if nova_senha:
                    self.cur.execute("UPDATE usuarios SET senha = %s WHERE matricula = %s", (nova_senha, matricula))
                self.conn.commit()
                print("Dados alterados com sucesso!")
            
            except Exception as error:
                print(f"Ocorreu um erro ao alterar os dados: {error}")
    
    
    def verificar_visto(self, nome: str, nacionalidade: str, data_nascimento: str, numero_visto: int, passaporte: int, tipo_visto: str, data_validade: str, pais_emitente: str):
        if nome and nacionalidade and data_nascimento and numero_visto and passaporte and tipo_visto and data_validade and pais_emitente:
            try:
                self.cur.execute("INSERT INTO passageiros (passaporte, nome, nacionalidade, data_nascimento) VALUES (%s, %s, %s, %s)", (passaporte, nome, nacionalidade, data_nascimento))
                self.cur.execute("INSERT INTO vistos (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade) VALUES (%s, %s, %s, %s, %s)", (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade))
                self.conn.commit()

            except Exception as error:
                print(f"Houve um erro ao validar o visto. Motivo: {error}")
                self.conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")
            
    # -> Método ainda falta ser finalizado
    def editar_visto(self, novo_nome: None, nova_nacionalidade: None, nova_data_nascimento: None, novo_numero_visto: None, novo_passaporte: None, novo_tipo_visto: None, nova_data_validade: None, novo_pais_emitente):
        try: 
            if novo_nome:
                self.cur.execute("UPDATE passageiros SET nome = %s", (novo_nome,))
            if nova_nacionalidade:
                self.cur.execute("UPDATE passageiros SET nacionalidade = %s", (nova_nacionalidade,))
            if nova_data_nascimento:
                self.cur.execute("UPDATE passageiros SET data_nascimento = %s", (nova_data_nascimento,))
            if novo_numero_visto:
                self.cur.execute("UPDATE passageiros SET numero_visto = %s", (novo_numero_visto,))
            if novo_passaporte:
                self.cur.execute("UPDATE passageiros SET novo_passaporte = %s", (novo_passaporte,))
            if novo_tipo_visto:
                self.cur.execute("UPDATE passageiros SET tipo_visto = %s", (novo_tipo_visto,))
            if nova_data_validade:
                self.cur.execute("UPDATE passageiros SET data_validade = %s", (nova_data_validade,))
            if novo_pais_emitente:
                self.cur.execute("UPDATE passageiros SET pais_emitente = %s", (novo_pais_emitente,))
            self.conn.commit()
        
        except Exception as error:
            print(f"Ocorreu um erro: {error}")
                
     
    def excluir_visto(self, numero_visto: str):
        if numero_visto:
            try:
                self.cur.execute("DELETE FROM passageiros WHERE numero_visto = %s", [numero_visto])
                self.conn.commit()

            except Exception as error:
                print(f"Houve um erro ao excluir o visto. Motivo: {error}")
                self.conn.rollback()
        else:
            print("Preencha todos os campos obrigatórios!")


    
