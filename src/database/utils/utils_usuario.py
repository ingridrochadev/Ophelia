import psycopg2
from os import getenv
from dotenv import load_dotenv
import bcrypt
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import string, random

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
            return False
        else:
            return True
    
    
    def criar_usuario(self, nome: str, cpf: str, email: str, senha: str, matricula: str, tipo_usuario: str):
        if nome and cpf and email and senha and matricula and tipo_usuario:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                hashed_senha = self.encriptar_senha( senha)
                
                # Verificar se o usuário já existe
                cur.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", (email, ))
                count = cur.fetchone()[0]
                verificacao = count > 0
                
                if not verificacao and self.validar_cpf(cpf) and self.validar_email(email) and self.validar_senha(senha):
                    cur.execute("INSERT INTO usuarios (nome, cpf, email, senha, matricula, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)", 
                                (nome, cpf, email, hashed_senha, matricula, tipo_usuario))
                    conn.commit()
                else:
                    print("Os dados informados não são válidos ou o usuário já existe! Tente novamente.")

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
    
    
    def verificar_tipo_e_nome_perfil(self, email):
        if email:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                cur.execute("SELECT tipo_usuario, nome FROM usuarios WHERE email = %s", (email, ))
                perfil, nome = cur.fetchone()
                
                if perfil == "Supervisor":
                    return 'admin', nome
                elif perfil == "Agente de Aeroporto":
                    return 'user', nome
                else:
                    pass
                    
            except Exception as error:
                print(f"Ocorreu um erro na tentativa de login. Motivo: {error}")
                return "Sem Acesso", None
            
            finally:
                cur.close()
                conn.close()
                
        else:
            return "Preencha todos os campos obrigatórios.", None
    
    
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
    
    
    def criar_codigo_confirmacao(self):
        caracteres = string.ascii_uppercase + string.digits
        codigo = ''.join(random.choice(caracteres) for _ in range(4))
        return codigo
    
    
    def enviar_confirmacao(self, email: str):
        conn = self.estabelecer_conexao()
        cur = conn.cursor()
        
        # Conexão com os servidores do google
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        smtp_user = 'ophelia.technology@gmail.com'
        smtp_password = 'btig znuw lnvc enrm'

        # Verifica se um email de confirmação já foi enviado anteriormente
        cur.execute("SELECT COUNT(*) FROM codigos_verificacao WHERE email = %s", (email,))
        count = cur.fetchone()[0]
        if count > 0:
            cur.execute("DELETE FROM codigos_verificacao WHERE email = %s", (email, ))
            conn.commit()

        # Gerando o código de confirmação
        codigo = self.criar_codigo_confirmacao()
        cur.execute("INSERT INTO codigos_verificacao (codigo, email) VALUES (%s, %s)", (codigo, email))
        conn.commit()
        
        # Criando a mensagem
        mensagem = f"""
<html>
  <head></head>
  <body>
    <p>Olá!</p>
    <p>Parece que você está tentando redefinir sua senha na Ophelia.</p>
    <p>Aqui está o código de verificação necessário:</p>
    <h1><strong>{codigo}</strong></h1>
  </body>
</html>
"""

        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = email
        msg['Subject'] = 'Solicitação de redefinição de senha'
        msg.attach(MIMEText(mensagem, 'html'))

        # Enviando o e-mail
        try:
            with smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) as server:
                server.login(smtp_user, smtp_password)
                server.send_message(msg)
            print("E-mail enviado com sucesso!")
        
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")
            
        finally:
                cur.close()
                conn.close()
    
    
    def confirmar_codigo(self, email: str, codigo_recebido: str):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
        
            cur.execute("SELECT codigo FROM codigos_verificacao WHERE email = %s", (email,))
            codigo_armazenado = cur.fetchone()[0]
            
            if codigo_recebido == codigo_armazenado:
                cur.execute("DELETE FROM codigos_verificacao WHERE codigo = %s", (codigo_recebido, ))
                conn.commit()
                return True, 'Código verificado com sucesso!'
            else:
                return False, 'O código não coincide'
                
        except Exception as error:
            return False, f"Erro ao confirmar código: {error}"
            
        finally:
                cur.close()
                conn.close()
    
    
    def redefinir_senha(self, email, codigo_confirmacao, nova_senha, nova_senha2):
        if email and codigo_confirmacao and nova_senha and nova_senha2:
            try:
                conn = self.estabelecer_conexao()
                cur = conn.cursor()
                
                codigo_confirmado = self.confirmar_codigo(email, codigo_confirmacao)[0]
                
                if codigo_confirmado:    
                    # Verifica se o email está cadastrado
                    cur.execute("SELECT senha FROM usuarios WHERE email = %s", (email, ))
                    usuario = cur.fetchone()
                    if usuario:
                        # Verifica se as senhas são iguais
                        if nova_senha == nova_senha2:
                            # Verificas se a senha é válida
                            senha_valida = self.validar_senha(nova_senha)
                            if senha_valida:
                                hashed_senha = self.encriptar_senha(nova_senha)
                                cur.execute("UPDATE usuarios SET senha = %s WHERE email = %s", (hashed_senha, email))
                                conn.commit()
                                return "Senha alterada com sucesso!"
                            else:
                                return 'Senha inválida! A senha deve conter letras minúsculas, maiúsculas, números, símbolos e ter no minimo 6 caracteres.'
                        else:
                            return "As senhas informadas não coincidem!"       
                    else: 
                        return "E-mail e/ou senha incorreta. Tente novamente!"
                else:
                    return "Código inválido!"
                
            except Exception as error:
                return f'Ocorreu um erro ao redefinir a senha: {error}'
                
            finally:
                cur.close()
                conn.close()
        else:
            return "Preencha todos os campos obrigatórios!"
        
        
    def listar_usuarios_default(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios")
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
    
    
    def listar_usuarios_asc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios ORDER BY nome")
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
            
            
    def listar_usuarios_desc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios ORDER BY nome DESC")
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
            
    
    def listar_usuarios_supervisor(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s", ("Supervisor", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
    
    
    def listar_usuarios_supervisor_asc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s ORDER BY nome", ("Supervisor", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
            
    
    def listar_usuarios_supervisor_desc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s ORDER BY nome DESC", ("Supervisor", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
    
    
    def listar_usuarios_agente(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s", ("Agente de Aeroporto", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
    
    
    def listar_usuarios_agente_asc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s ORDER BY nome", ("Agente de Aeroporto", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()
            
    
    def listar_usuarios_agente_desc(self):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT matricula, nome, email, cpf, tipo_usuario FROM usuarios WHERE tipo_usuario = %s ORDER BY nome DESC", ("Agente de Aeroporto", ))
            usuarios = cur.fetchall()
            return usuarios
        
        except Exception as error:
            print(f"Ocorreu um erro ao listar os usuários: {error}")
        
        finally:
            cur.close()
            conn.close()    
        
        
    def buscar_usuario(self, matricula):
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            cur.execute("SELECT nome, cpf, email, senha, tipo_usuario FROM usuarios WHERE matricula = %s", (matricula, ))
            usuario = cur.fetchone()
            return usuario
        
        except Exception as error:
            return f"Ocorreu um erro ao buscar usuário: {error}"
        finally:
            cur.close()
            conn.close()
            
            
    def alterar_usuario(self, matricula, dados):
        nome, cpf, email, tipo = dados
        try:
            conn = self.estabelecer_conexao()
            cur = conn.cursor()
            
            if nome:
                cur.execute("UPDATE usuarios SET nome = %s WHERE matricula = %s", (nome, matricula))
                conn.commit()
            if cpf:
                cpf_valido = self.validar_cpf(cpf)
                if cpf_valido:
                    cur.execute("UPDATE usuarios SET cpf = %s WHERE matricula = %s", (cpf, matricula))
                    conn.commit()
                else:
                    return "CPF inválido! Tente novamente."
            if email:
                email_valido = self.validar_email(email)
                if email_valido:
                    cur.execute("UPDATE usuarios SET email = %s WHERE matricula = %s", (email, matricula))
                    conn.commit()
                else:
                    return "E-mail inválido! Tente novamente."
            if tipo:
                cur.execute("UPDATE usuarios SET tipo_usuario = %s WHERE matricula = %s", (tipo, matricula))
                conn.commit()
                
            return 'Usuário alterado com sucesso!'
        
        except Exception as error:
            return f'Ocorreu um erro ao alterar o usuário: {error}'
        finally:
            cur.close()
            conn.close()    


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
