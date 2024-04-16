import dependencies as d

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
