from src.image_processing import dependencies as d

import src.image_processing.dependencies as d

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

    # Inicializa as variáveis para armazenar as informações
    name = ''
    passport_number = ''
    nationality = ''
    dob = None
    expiry_date = None
    passport_type = ''
    issuing_country = ''
    visa_number = ''

    if mrz:  # Verifica se a lista mrz não está vazia
        if mrz[0].startswith('VNUSA'):  # Verifica se o MRZ começa com 'VNUSA'
            parts = mrz[0][5:25].split('<')
            name =' '.join(parts)
            name = name.replace('VNUSA', ' ').replace('<', ' ')
        else:
            name = (mrz[0][4:20] + " " + mrz[0][20:30]).replace('<', ' ').strip()
            name = name.replace('VNUSA', ' ').replace('<', ' ')

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

    # Formate as datas para remover as partes de hora e minuto e a representação "datetime.datetime"
    dob_str = dob.strftime('%Y-%m-%d') if dob else None
    expiry_date_str = expiry_date.strftime('%Y-%m-%d') if expiry_date else None

    # Remove o caractere de nova linha (\n) da última string
    visa_number = visa_number.rstrip('\n')

    # Crie um array com todas as variáveis formatadas
    infor = [name, passport_number, nationality, dob_str, expiry_date_str, passport_type, issuing_country, visa_number]

    return infor

# Uso:
image_path = 'imagem\\visto5.jpg'
infor = leitura_do_passaporte(image_path)
print(infor)