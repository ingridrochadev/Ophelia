from .tabelas import Sistema
import streamlit as st

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
                st.success("Dados alterados com sucesso!")
            
            except Exception as error:
                st.error(f"Ocorreu um erro ao alterar os dados: {error}")
    
    
    def verificar_visto(self, nome: str, nacionalidade: str, data_nascimento: str, numero_visto: int, passaporte: int, tipo_visto: str, data_validade: str, pais_emitente: str):
        if nome and nacionalidade and data_nascimento and numero_visto and passaporte and tipo_visto and data_validade and pais_emitente:
            try:
                self.cur.execute("INSERT INTO passageiros (passaporte, nome, nacionalidade, data_nascimento) VALUES (%s, %s, %s, %s)", (passaporte, nome, nacionalidade, data_nascimento))
                self.cur.execute("INSERT INTO vistos (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade) VALUES (%s, %s, %s, %s, %s)", (numero_visto, passaporte, tipo_visto, pais_emitente, data_validade))
                self.conn.commit()

            except Exception as error:
                st.error(f"Houve um erro ao validar o visto. Motivo: {error}")
                self.conn.rollback()
        else:
            st.error("Preencha todos os campos obrigatórios!")
            
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
            st.error(f"Ocorreu um erro: {error}")
                
     
    def excluir_visto(self, numero_visto: str):
        if numero_visto:
            try:
                self.cur.execute("DELETE FROM passageiros WHERE numero_visto = %s", [numero_visto])
                self.conn.commit()

            except Exception as error:
                st.error(f"Houve um erro ao excluir o visto. Motivo: {error}")
                self.conn.rollback()
        else:
            st.error("Preencha todos os campos obrigatórios!")


    