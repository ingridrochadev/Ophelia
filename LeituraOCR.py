import cv2
import pytesseract
import re

# Função para extrair texto de uma imagem usando OCR
def extract_text_from_image(image_path):
    # Carregar a imagem usando OpenCV
    image = cv2.imread(image_path)
    
    # Converter a imagem para tons de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplicar uma limiarização para tornar o texto mais proeminente
    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Executar OCR na imagem
    extracted_text = pytesseract.image_to_string(threshold_image)
    
    return extracted_text

# Função para salvar texto em um arquivo
def save_text_to_file(text, output_file):
    with open(output_file, 'w') as file:
        file.write(text)

# Função para extrair informações do visto com base em padrões definidos
def extrair_informacoes_visto(texto):
    informacoes = {}
    for chave, padrao in padroes.items():
        correspondencia = re.search(padrao, texto, re.IGNORECASE)
        if correspondencia:
            informacoes[chave] = correspondencia.group(1)
    return informacoes

if __name__ == "__main__":
    # Caminho para a imagem do visto
    image_path = "imagem\\visto8.png"
    
    # Extrair texto da imagem
    extracted_text = extract_text_from_image(image_path)
    
    # Salvar texto em um arquivo
    output_file = "visto_texto_extraido1.txt"
    save_text_to_file(extracted_text, output_file)
    
    print("Texto extraído e salvo com sucesso!")

    # Padrões para extrair informações do visto
    padroes = {
        'Issuing Post Name': r"Issuing Post Name\s*:\s*(\w+)",
        'Surname': r"Surname\s*:\s*(\w+)",
        'Given Name': r"Given Name\s*:\s*(\w+)",
        'Passport Number': r"Passport Number\s*:\s*(\w+)",
        'Entries': r"Entries\s*:\s*(\d+)",
        'Annotation': r"Annotation\s*:\s*(.+)",
        'Issue Date': r"Issue Date\s*:\s*(\d{2}/\d{2}/\d{4})",
        'Sex': r"Sex\s*:\s*(Male|Female)",
        'Control Number': r"Control Number\s*:\s*(\d+)",
        'Visa Type/Class': r"Visa Type/Class\s*:\s*(\w+)",
        'Birth Date': r"Birth Date\s*:\s*(\d{2}/\d{2}/\d{4})",
        'Nationality': r"Nationality\s*:\s*(\w+)",
        'Expiration Date': r"Expiration Date\s*:\s*(\d{2}/\d{2}/\d{4})"
    }

    # Extrair informações do visto
    informacoes_visto = extrair_informacoes_visto(extracted_text)
    
    # Imprimir informações do visto
    print("\nInformações do visto:")
    for chave, valor in informacoes_visto.items():
        print(f"{chave}: {valor}")
