from src.image_processing import dependencies as d

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
        file.write(f"Nome: {name}\n")
        file.write(f"Numero de passaporte: {passport_number}\n")
        file.write(f"Nacionalidade: {nationality}\n")
        file.write(f"Data de aniversario: {dob.strftime('%Y-%m-%d')}\n")
        file.write(f"Sexo: {sex}\n")
        file.write(f"Data de Validade: {expiry_date.strftime('%Y-%m-%d')}\n")
        file.write(f"Tipo de passaporte: {passport_type}\n")
        file.write(f"Cidade Emitente: {issuing_country}\n")
        file.write(f"Numero do visto: {visa_number}\n")

#Uso:
image_path = 'imagem\\visto1.jpg'
leitura_do_passaporte(image_path)


def verificar_embarque(tipo_de_visto, validade_visto, data_nascimento):
    
    def return_age(date: d.datetime) -> tuple:
        today = d.datetime.now()
        age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
        is_adult = age >= 18
        return age, is_adult

    def check_validity(visa_validity: d.datetime) -> bool:
        today = d.datetime.now()
        return today > visa_validity
    
    if not isinstance(validade_visto, d.datetime):
        print("A validade do visto deve ser um objeto datetime.")
        return

    if check_validity(validade_visto):
        print("O visto está fora da validade. Proibido o embarque.")
        return

    idade, is_adult = return_age(data_nascimento)
    if is_adult:
        print("A idade é:", idade, "anos. É maior de idade.")
    else:
        print("A idade é:", idade, "anos. É menor de idade. Precisa de autorização dos pais.")

    # Verifica se o visto está dentro da validade
    if validade_visto < d.datetime.now():
        print("O visto está fora da validade")
    else:
        print("O visto ainda está válido")

    if tipo_de_visto.lower() in ["b1", "b2", "b3"]:
        print('Visto de embarque para turismo, visitas a amigos ou parentes, tratamento médico, etc.')
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        elif tipo_de_visto.lower() == "b1" and "empregado doméstico" in validade_visto.lower():
            print("Verificar se o empregado doméstico está acompanhado do seu empregador.")
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "c1":
        print("Visto de trânsito.\nVerificar se o destino final é em outro país e não nos EUA para poder entrar nos EUA para fazer conexão.")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")        
            
    elif tipo_de_visto.lower() == "f1" or tipo_de_visto.lower() == "m1" or tipo_de_visto.lower()== "m":
        print("Visto de embarque para estudantes matriculados em instituições acadêmicas ou estudantes não academicos Limitado a instituições educacionais específicas.\nVerificar o documento de Formulário I-20 da instituição educacional.")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")
            
    elif tipo_de_visto.lower() == "j1":
        print("Visto de embarque para participantes de programas de intercâmbio.\nVerificar o documento: carta programa de intercâmbio.")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "h1b":
        print("Visto de embarque para profissionais estrangeiros em ocupações especializadas.\nVerificar o documento de contrato de trabalho ou oferta de emprego válida.")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "l1":
        print("Visto de embarque para funcionários de empresas multinacionais transferidos.\nVerificar o documento: carta de transferencia da empresa multinacional")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "o1":
        print("Visto de embarque para pessoas com habilidades extraordinárias ou realizações notáveis.\nVerificar o documento de comprovante de habilidades extraordinárias")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "e1":
        print("Visto de embarque para comerciantes de países com tratados de comércio.\nVerificar o documento: provas comércio")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "e2":
        print("Visto de embarque para investidores de países com tratados de comércio.\nVerificar o documento: provas investimento")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "k1":
        print("Visto de embarque para noivos ou noivas de cidadãos americanos para casar em 90 dias.\nVerificar o documento: processo de casamento")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "a1" or tipo_de_visto.lower() == "a2":
        print("Visto de embarque para diplomatas e funcionários de governos estrangeiros.\nVerificar o documento: diploma diplomático")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "g1" or tipo_de_visto.lower() == "g2" or tipo_de_visto.lower() == "g3" or tipo_de_visto.lower() == "g4" or tipo_de_visto.lower() == "g5":
        print("Visto de embarque para funcionários de organizações internacionais.\nVerificar o documento: carta organização internacional")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "r1":
        print("Visto de embarque para trabalhadores religiosos.\nVerificar o documento: provas de afiliação religiosa")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "t"or tipo_de_visto.lower() == "to":
        print("Visto de embarque para vítimas de tráfico humano.\nVerificar o documento: provas vítima tráfico humano")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "u":
        print("Visto de embarque para vítimas de crimes.\nVerificar o documento de provas vítima de crime")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "v":
        print("Visto de embarque para cônjuges ou filhos de residentes legais permanentes.\nVerificar o documento: provas de relacionamento")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "d":
        print("Visto de embarque para tripulantes de navios ou aeronaves.\nVerificar o documento de licença tripulação")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "nato":
        print("Visto de embarque para membros da OTAN e suas famílias.\nVerificar o documento:identificação OTAN")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "p1":
        print("Visto de atleta/artista de destaque.\n Verificar documentação que comprove status de atleta ou artista de destaque")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "tn":
        print("Visto do Acordo de Livre Comércio da América do Norte (NAFTA)")
        if not check_validity(validade_visto) and is_adult:
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")  

    else:
        print("Não é permitido embarcar. Verifique seu tipo de visto.")


if __name__ == '__main__':
    # Informações extraídas do visto
    with open('informacoes.txt', 'r') as file:
        lines = file.readlines()

    # Extraindo as informações
    tipo_de_visto = lines[7].split(": ")[1].strip()
    
    # Removendo a hora da data de validade, se presente
    expiry_date_str = lines[6].split(": ")[1].strip().split()[0]  # Remove a hora, se presente
    expiry_date = d.datetime.strptime(expiry_date_str, "%Y-%m-%d")
    
    # Parsing da data de nascimento
    data_nascimento_str = lines[4].split(": ")[1].strip()
    
    # Se a data contiver a hora, remova a parte da hora
    if len(data_nascimento_str) > 10:
        data_nascimento_str = data_nascimento_str.split()[0]
    
    data_nascimento = d.datetime.strptime(data_nascimento_str, "%Y-%m-%d")

    # Chamando as funções com as informações extraídas
    verificar_embarque(tipo_de_visto, expiry_date, data_nascimento)

