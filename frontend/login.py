import streamlit as st
from PIL import Image
import os

def tela_login():
    # Função para verificar login
    def verificar_login(usuario, senha):
        if email_recebido == email and senha_recebida == senha:
            return True
        else:
            return False

    # Logo
    logo = Image.open("Logo transparente.png")
    logo_container = st.empty()

    # Tela de login
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(logo, width=150)
    with col2:
        st.markdown("<h1 style='text-align: left; color: purple;'>Ophelia</h1>", unsafe_allow_html=True)
    st.markdown('----')

    # Formulário de login
    form = st.form(key='login')
    email_recebido = form.text_input(label="Email")
    senha_recebida = form.text_input(label="Senha", type="password")
    botao_login = form.form_submit_button(label="Entrar")

    # Verificação de login
    if botao_login:
        if verificar_login(email, senha):
            st.success("Login realizado com sucesso!")
            # Código para direcionar para a página principal após o login
        else:
            st.error("Usuário ou senha inválidos.")

    # Adicionando o link para registrar-se
    st.markdown("Não tem uma conta? Clique [aqui](/register_user.py)")

tela_login()