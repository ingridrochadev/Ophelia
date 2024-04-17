import streamlit as st
from src.pages.utils import Sistema

def tela_register():
    # Tela de cadastro de usuário
    st.markdown("<h1 style='text-align: center; color: purple;'>Cadastro de Usuário</h1>", unsafe_allow_html=True)
    st.markdown('----')

    # Formulário de cadastro
    with st.form(key='cadastro_usuario'):
        nome_completo = st.text_input(label="Nome Completo")
        email = st.text_input(label="Email")
        senha = st.text_input(label="Senha", type="password")
        cpf = st.text_input(label="CPF - Somente números")
        matricula = st.text_input(label="Matrícula do Funcionário")

        botao_adicionar = st.form_submit_button(label="Adicionar")

        # Verificação de cadastro
        if botao_adicionar:
            if nome_completo.strip() == "" or email.strip() == "" or senha.strip() == "" or cpf.strip() == "" or matricula.strip() == "":
                st.error("Por favor, preencha todos os campos.")
            else:
                sistema = Sistema()  # Instancia a classe Sistema
                sistema.criar_usuario(nome_completo, cpf, email, senha, matricula)
                st.success("Usuário cadastrado com sucesso!")