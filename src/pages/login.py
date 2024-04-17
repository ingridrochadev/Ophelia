from PIL import Image
import streamlit as st
from src.pages.utils import Sistema
from src.pages.register_user import tela_register

def tela_login():
    
    logo = Image.open("src/pages/Logo transparente.png")
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
        sistema = Sistema()  # Instancia a classe Sistema
        sistema.fazer_login(email_recebido, senha_recebida)

    # Adicionando o link para registrar-se
    st.button("Não tem uma conta? Clique aqui", on_click=tela_register())