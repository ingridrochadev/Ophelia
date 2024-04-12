import streamlit as st

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

        botao_cadastrar = st.form_submit_button(label="Cadastrar")

        # Verificação de cadastro
        if botao_cadastrar:
            if nome_completo.strip() == "" or email.strip() == "" or senha.strip() == "" or cpf.strip() == "" or matricula.strip() == "":
                st.error("Por favor, preencha todos os campos.")
            else:
                st.success("Usuário cadastrado com sucesso!")
    
    return nome_completo, email, senha, cpf, matricula

tela_register()