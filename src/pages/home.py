import streamlit as st
from PIL import Image  # Supondo que você tenha um arquivo database.py com as funcionalidades de banco de dados
# from src.pages.utils import Sistema

def tela_home(nome_usuario):
    
    st.write("----")
    

    st.sidebar.markdown(f"<h1 style='text-align: left; color: purple;'>Bem-vindo(a), {nome_usuario}!</h1>", unsafe_allow_html=True)
    st.sidebar.button("Editar Perfil")
    st.sidebar.button("Logout")
    st.sidebar.write("----")
    
    filtro_selecionado = st.sidebar.selectbox('Filtrar por', ['Todos os vistos', 'Vistos aprovados', 'Vistos negados'])
    if filtro_selecionado == 'Vistos aprovados':
        st.markdown(f"<h1 style='text-align: left; color: purple;'>Vistos aprovados</h1>", unsafe_allow_html=True)
        st.selectbox("Ordenar", ["A-Z", 'Mais recentes', "Z-A"])
    elif filtro_selecionado == 'Vistos negados':
        st.markdown(f"<h1 style='text-align: left; color: purple;'>Vistos negados</h1>", unsafe_allow_html=True)
        st.selectbox("Ordenar", ["A-Z", 'Mais recentes', "Z-A"])
    elif filtro_selecionado == 'Todos os vistos':
        st.markdown(f"<h1 style='text-align: left; color: purple;'>Todos os vistos</h1>", unsafe_allow_html=True)
        st.selectbox("Ordenar", ["A-Z", 'Mais recentes', "Z-A"])
        
    # # Exibindo nomes e informações
    # nomes = database.obter_nomes()  # Supondo que a função obter_nomes() retorna uma lista de nomes do banco de dados
    # for nome in nomes:
    #     if st.button(nome):
    #         # Exibir informações da pessoa
    #         informacoes = database.obter_informacoes(nome)  # Supondo que a função obter_informacoes(nome) retorna as informações da pessoa
    #         st.write(f"Informações de {nome}: {informacoes}")

tela_home('Ingrid')
