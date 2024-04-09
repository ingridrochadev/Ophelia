def verificar_embarque(tipo_de_visto, validade_visto, proposito_viagem, documentacao_suporte):

    if tipo_de_visto.lower() == "b-1" or tipo_de_visto == "b-2":
        print('Visto de embarque para turismo, visitas a amigos ou parentes, tratamento médico, etc.')
        if validade_visto == "válido" and proposito_viagem in ["turismo", "visitas", "tratamento médico"]:
            print("Documentação verificada. Embarque permitido.")
        elif tipo_de_visto.lower() == "b-1"and proposito_viagem in["empregado domestico"]:
              print("Verificar se o empregado doméstico está acompanhado do seu empregador.\nDocumentação verificada. Embarque permitido.")  
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "c-1":
        print("Visto de trânsito.\nVerificar se o destino final é em outro país e não nos EUA para poder entrar nos EUA para fazer conexão.")
        if validade_visto == "válido" and proposito_viagem == "trânsito" and documentacao_suporte == "passaporte com destino final sem ser EUA":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")        
            
    elif tipo_de_visto.lower() == "f-1" or tipo_de_visto.lower() == "m-1" or tipo_de_visto.lower()== "m":
        print("Visto de embarque para estudantes matriculados em instituições acadêmicas ou estudantes não academicos Limitado a instituições educacionais específicas.\nVerificar o documento de Formulário I-20 da instituição educacional.")
        if validade_visto == "válido" and proposito_viagem == "estudo" and documentacao_suporte == "Formulário I-20 da instituição educacional":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")
            
    elif tipo_de_visto.lower() == "j-1":
        print("Visto de embarque para participantes de programas de intercâmbio.\nVerificar o documento: carta programa de intercâmbio.")
        if validade_visto == "válido" and proposito_viagem == "intercâmbio" and documentacao_suporte == "carta programa intercâmbio":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "h-1b":
        print("Visto de embarque para profissionais estrangeiros em ocupações especializadas.\nVerificar o documento de contrato de trabalho ou oferta de emprego válida.")
        if validade_visto == "válido" and proposito_viagem == "trabalho" and documentacao_suporte == "Carta de trabalho ou oferta de emprego válida":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "l-1":
        print("Visto de embarque para funcionários de empresas multinacionais transferidos.\nVerificar o documento: carta de transferencia da empresa multinacional")
        if validade_visto == "válido" and proposito_viagem == "transferência" and documentacao_suporte == "carta de transferencia da empresa multinacional":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "o-1":
        print("Visto de embarque para pessoas com habilidades extraordinárias ou realizações notáveis.\nVerificar o documento de comprovante de habilidades extraordinárias")
        if validade_visto == "válido" and proposito_viagem == "habilidades extraordinárias" and documentacao_suporte == "comprovante de habilidades extraordinárias":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "e-1":
        print("Visto de embarque para comerciantes de países com tratados de comércio.\nVerificar o documento: provas comércio")
        if validade_visto == "válido" and proposito_viagem == "comércio" and documentacao_suporte == "provas comércio":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "e-2":
        print("Visto de embarque para investidores de países com tratados de comércio.\nVerificar o documento: provas investimento")
        if validade_visto == "válido" and proposito_viagem == "investimento" and documentacao_suporte == "provas investimento":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "k-1":
        print("Visto de embarque para noivos ou noivas de cidadãos americanos para casar em 90 dias.\nVerificar o documento: processo de casamento")
        if validade_visto == "válido" and proposito_viagem == "casamento" and documentacao_suporte == "processo de casamento":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "a-1" or tipo_de_visto.lower() == "a-2":
        print("Visto de embarque para diplomatas e funcionários de governos estrangeiros.\nVerificar o documento: diploma diplomático")
        if validade_visto == "válido" and proposito_viagem == "serviço diplomático" and documentacao_suporte == "diploma diplomático":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "g-1" or tipo_de_visto.lower() == "g-2" or tipo_de_visto.lower() == "g-3" or tipo_de_visto.lower() == "g-4" or tipo_de_visto.lower() == "g-5":
        print("Visto de embarque para funcionários de organizações internacionais.\nVerificar o documento: carta organização internacional")
        if validade_visto == "válido" and proposito_viagem == "serviço internacional" and documentacao_suporte == "carta organização internacional":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "r-1":
        print("Visto de embarque para trabalhadores religiosos.\nVerificar o documento: provas de afiliação religiosa")
        if validade_visto == "válido" and proposito_viagem == "trabalho religioso" and documentacao_suporte == "provas de afiliação religiosa":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "t":
        print("Visto de embarque para vítimas de tráfico humano.\nVerificar o documento: provas vítima tráfico humano")
        if validade_visto == "válido" and proposito_viagem == "vítima tráfico humano" and documentacao_suporte == "provas vítima tráfico humano":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "u":
        print("Visto de embarque para vítimas de crimes.\nVerificar o documento de provas vítima de crime")
        if validade_visto == "válido" and proposito_viagem == "vítima de crime" and documentacao_suporte == "provas vítima de crime":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "v":
        print("Visto de embarque para cônjuges ou filhos de residentes legais permanentes.\nVerificar o documento: provas de relacionamento")
        if validade_visto == "válido" and proposito_viagem == "reunião familiar" and documentacao_suporte == "provas de relacionamento":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "d":
        print("Visto de embarque para tripulantes de navios ou aeronaves.\nVerificar o documento de licença tripulação")
        if validade_visto == "válido" and proposito_viagem == "serviço de tripulação" and documentacao_suporte == "licença tripulação":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "nato":
        print("Visto de embarque para membros da OTAN e suas famílias.\nVerificar o documento:identificação OTAN")
        if validade_visto == "válido" and proposito_viagem == "membro da OTAN" and documentacao_suporte == "identificação OTAN":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "p-1":
        print("Visto de atleta/artista de destaque.\n Verificar documentação que comprove status de atleta ou artista de destaque")
        if validade_visto == "válido" and proposito_viagem == "status" and documentacao_suporte == "Documentação que comprove status de atleta ou artista de destaque":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")

    elif tipo_de_visto.lower() == "tn":
        print("Visto do Acordo de Livre Comércio da América do Norte (NAFTA)")
        if validade_visto == "válido" and proposito_viagem == "NAFTA":
            print("Documentação verificada. Embarque permitido.")
        else:
            print("Restrições de visto ou documentação inadequada. Embarque não permitido.")  

    else:
        print("Não é permitido embarcar. Verifique seu tipo de visto.")


tipo_de_visto_passageiro = "B-1"
validade_visto_passageiro = "válido"
proposito_viagem_passageiro = "empregado domestico"
documentacao_suporte_passageiro = "carta convite"
verificar_embarque(tipo_de_visto_passageiro, validade_visto_passageiro, proposito_viagem_passageiro, documentacao_suporte_passageiro)
