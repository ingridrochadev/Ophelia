import streamlit as st
from src.image_processing import JUNCAO_OCR_E_TIPOVISTO

def photo():
    
    # Título do aplicativo
    st.markdown("<h1 style='text-align: left; color: purple;'>Adicione um visto</h1>", unsafe_allow_html=True)

    # Componente de upload de arquivo
    uploaded_image = st.file_uploader("Escolha um arquivo", type=['jpg', 'jpeg', 'png', 'webp'])
        
    picture = st.camera_input("Ou tire uma foto")

    # Verificação se um arquivo foi carregado
    if uploaded_image is not None:
        # Processamento do arquivo carregado
        JUNCAO_OCR_E_TIPOVISTO.leitura_do_passaporte(uploaded_image)
        st.image(uploaded_image, caption='Imagem carregada', use_column_width=True)

photo()
