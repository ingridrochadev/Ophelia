import cv2 
import pytesseract 
import pandas as pd 
import numpy as np 
import math 
from matplotlib import pyplot as plt

# Carrega a imagem
img = cv2.imread('imagem\\visto7.jpg', 0)
img_copy = img.copy() 

# Aplica Canny edge detection
img_canny = cv2.Canny(img_copy, 30 , 80, apertureSize=3)

# Mostra a imagem após Canny edge detection
plt.imshow(img_canny, cmap='gray')
plt.title('Imagem após Canny Edge Detection')
plt.show()

# Detecta linhas usando a transformada de Hough
img_hough = cv2.HoughLinesP(img_canny, 1, math.pi / 180, 100, minLineLength=100, maxLineGap=10)


# Recorta a região de interesse (ROI)
(x, y, w, h) = (np.amin(img_hough, axis=0)[0, 0], np.amin(img_hough, axis=0)[0, 1], 
                np.amax(img_hough, axis=0)[0, 0] - np.amin(img_hough, axis=0)[0, 0], 
                np.amax(img_hough, axis=0)[0, 1] - np.amin(img_hough, axis=0)[0, 1])
img_roi = img_copy[y:y+h, x:x+w]

# Pré-processamento da ROI para OCR
(height, width) = img_roi.shape
img_roi_copy = img_roi.copy()
dim_mrz = (x, y, w, h) = (1, round(height*0.8), width-3, round(height-(height*0.7))-2)

#desenhar retângulo na ROI
img_roi_copy = cv2.rectangle(img_roi_copy, (x, y), (x + w ,y + h),(0,0,0),2)

# Exibir imagem após desenhar retângulo
plt.imshow(cv2.cvtColor(img_roi_copy, cv2.COLOR_BGR2RGB))
plt.title('ROI com retângulo')
plt.axis('off')
plt.show()

#extrai o ROI
img_mrz = img_roi[y:y+h, x:x+w]

# Suavizar a imagem com filtro Gaussiano
img_mrz_blurred =cv2.GaussianBlur(img_mrz, (3,3), 0)

# Exibir imagem após aplicar filtro Gaussiano
plt.imshow(cv2.cvtColor(img_mrz_blurred, cv2.COLOR_BGR2RGB))
plt.title('ROI suavizada')
plt.axis('off')
plt.show()

# Aplicar limiar para binarizar a imagem
ret, img_mrz_thresh = cv2.threshold(img_mrz_blurred, 127, 255, cv2.THRESH_TOZERO)

# Exibir imagem após aplicar limiar
plt.imshow(cv2.cvtColor(img_mrz_thresh, cv2.COLOR_BGR2RGB))
plt.title('ROI binarizada')
plt.axis('off')
plt.show()

# Realiza OCR na ROI pré-processada para extrair informações do MRZ
mrz = pytesseract.image_to_string(img_mrz, config = '--psm 12')

# Exibir a imagem após esta etapa
plt.imshow(cv2.cvtColor(img_mrz, cv2.COLOR_BGR2RGB))
plt.title('ROI após OCR')
plt.axis('off')
plt.show()

# Processa o texto extraído do MRZ
mrz = [line for line in mrz.split('\n') if len(line) > 10]

if mrz:  # Verifica se a lista mrz não está vazia
    if mrz[0][0:2] == 'P<':
        parts = mrz[0].split('<')
        lastname = mrz[0].split('<')[0][5:14]  # Extrai o sobrenome
        firstname = mrz[0].split('<')[1][0:10].replace('<', ' ').strip()  # Extrai o primeiro nome
    else:
        lastname = mrz[0][5:14].replace('<', ' ').strip()  # Extrai o sobrenome
        firstname_part = mrz[0][14:36].replace('<', ' ').strip() if len(mrz[0]) >= 36 else None  # Extrai o primeiro nome
        firstname = firstname_part if firstname_part and not firstname_part.isspace() else None

if len(mrz) > 1:  # Se houver uma segunda linha MRZ
    passport_number = mrz[1][0:8]  # Extrai o número do passaporte
    nationality = mrz[1][10:13]  # Extrai a nacionalidade
    dob = mrz[1][13:19]  # Extrai a data de nascimento
    sex = mrz[1][20]  # Extrai o sexo
    expiry_date = mrz[1][21:27]  # Extrai a data de validade
    passport_type = mrz[1][28:30]  # Extrai o tipo de passaporte
    issuing_country = mrz[1][30:33]  # Extrai o país emitente


# Salva as informações extraídas em um arquivo TXT
with open('informacoes.txt', 'w') as file:
    file.write(f"Sobrenome: {lastname}\n")
    file.write(f"Primeiro Nome: {firstname}\n")
    file.write(f"Numero de passaporte: {passport_number}\n")
    file.write(f"Nacionalidade: {nationality}\n")
    file.write(f"Data de aniversario: {dob}\n")
    file.write(f"Sexo: {sex}\n")
    file.write(f"Data de Validade: {expiry_date}\n")
    file.write(f"Tipo de passaporte: {passport_type}\n")
    file.write(f"Pais Emitente: {issuing_country}\n")
