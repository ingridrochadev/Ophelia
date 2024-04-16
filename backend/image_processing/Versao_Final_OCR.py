import dependencies as d

def leitura_do_passaporte(image_path):
    # Carrega a imagem
    img = d.cv2.imread(image_path)

    # Converte a imagem para escala de cinza
    img_gray = d.cv2.cvtColor(img, d.cv2.COLOR_BGR2GRAY)

    # Faz a cópia dessa imagem
    img_copy = img.copy() 

    # Aplica Canny edge detection
    img_canny = d.cv2.Canny(img_gray, 30, 80, apertureSize=3)

    # Detecta linhas usando a transformada de Hough
    img_hough = d.cv2.HoughLinesP(img_canny, 1, d.math.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Recorta a região de interesse (ROI)
    (x, y, w, h) = (d.np.amin(img_hough, axis=0)[0, 0], d.np.amin(img_hough, axis=0)[0, 1], 
                    d.np.amax(img_hough, axis=0)[0, 0] - d.np.amin(img_hough, axis=0)[0, 0], 
                    d.np.amax(img_hough, axis=0)[0, 1] - d.np.amin(img_hough, axis=0)[0, 1])
    img_roi = img_copy[y:y+h, x:x+w]

    # Pré-processamento da ROI para OCR
    height, width, _ = img_roi.shape  # Obter as dimensões da imagem ROI
    x = 1
    y = round(height * 0.8)
    w = width - 3
    h = round(height - (height * 0.7)) - 2

    # Extrai o ROI
    img_mrz = img_roi[y:y+h, x:x+w]

    # Suavizar a imagem com filtro Gaussiano
    img_mrz_blurred = d.cv2.GaussianBlur(img_mrz, (3, 3), 0)

    # Aplicar limiar para binarizar a imagem
    _, img_mrz_thresh = d.cv2.threshold(img_mrz_blurred, 127, 255, d.cv2.THRESH_TOZERO)

    # Realiza OCR na ROI pré-processada para extrair informações do MRZ
    mrz = d.pytesseract.image_to_string(img_mrz_thresh, config='--psm 12')


    # Processa o texto extraído do MRZ
    mrz = [line for line in mrz.split('\n') if len(line) > 10]

    if mrz:  # Verifica se a lista mrz não está vazia
        if mrz[0][0:2] == 'P<':
            parts = mrz[0].split('<')
            lastname = mrz[0].split('<')[0][5:]  # Extrai o sobrenome
            firstname = mrz[0].split('<')[1][0:10].replace('<', ' ').strip()  # Extrai o primeiro nome
        else:
            lastname = mrz[0][5:12].replace('<', ' ').strip()  # Extrai o sobrenome
            firstname_part = mrz[0][11:].replace('<', ' ').strip() if len(mrz[0]) >= 36 else None  # Extrai o primeiro nome
            firstname = firstname_part if firstname_part and not firstname_part.isspace() else None

    if len(mrz) > 1:  # Se houver uma segunda linha MRZ
        passport_number = mrz[1][0:8]  # Extrai o número do passaporte
        nationality = mrz[1][10:13]  # Extrai a nacionalidade
        dob = d.datetime.strptime(mrz[1][13:19], "%y%m%d")  # Extrai a data de nascimento
        current_year = d.datetime.now().year
        # Correção do ano de acordo com diferentes condições
        if dob.year < current_year - 30:
            dob = dob.replace(year=dob.year)
        elif dob.year < current_year - 24:
            dob = dob.replace(year=dob.year + 1900)
        else:
            dob = dob.replace(year=dob.year - 100)
        sex = mrz[1][20]  # Extrai o sexo
        expiry_date = d.datetime.strptime(mrz[1][21:27], "%y%m%d")  # Extrai a data de validade
        expiry_date = expiry_date.replace(year=expiry_date.year + 1900 if expiry_date.year < current_year - 24 else expiry_date.year)  # Corrige o ano
        passport_type = mrz[1][28:30]  # Extrai o tipo de passaporte
        issuing_country = mrz[1][30:33]  # Extrai o país emitente

    # Converte a imagem OpenCV para o formato do PIL
    img_copy_pil = d.Image.fromarray(d.cv2.cvtColor(img, d.cv2.COLOR_BGR2RGB))

    # Define o tamanho desejado para as imagens
    new_size = (700, 480)

    # Redimensiona a imagem para o tamanho desejado
    img_resized = img_copy_pil.resize(new_size)

    # Realiza o corte na imagem para extrair a região do MRZ
    cropped_img = img_resized.crop((500, 305, 660, 340))

    # Salva o texto extraído da região do número do visto (MRZ) em uma variável
    visa_number = d.pytesseract.image_to_string(cropped_img)

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
        file.write(f"Numero do visto: {visa_number}\n")

#Uso:
image_path = 'imagem\\visto1.jpg'
leitura_do_passaporte(image_path)
