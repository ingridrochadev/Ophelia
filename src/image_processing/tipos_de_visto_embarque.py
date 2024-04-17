#from datetime import datetime
#from dateutil.relativedelta import relativedelta

import dependencies as d

vistos = [
    # proposito_viagem              tipo_de_visto   documentacao_suporte
    ("empregado domestico",                 "b-1",  "carta convite"),
    ("visitas",                             "b-1",  "None"),
    ("turismo",                             "b-2",  "None"),
    ("tratamento médico",                   "b-2",  "None"),
    ("trânsito",                            "c-1",  "passaporte com destino final sem ser EUA"),
    ("estudo",                              "f",    "Formulário I-20 da instituição educacional"),
    ("estudo sem idiomas",                  "m",    "Formulário I-20 da instituição educacional"),
    ("intercâmbio",                         "j-1",  "carta programa intercâmbio"),
    ("trabalho",                            "h-1b", "Carta de trabalho ou oferta de emprego válida"),
    ("transferência",                       "l-1",  "carta de transferencia da empresa multinacional"),
    ("habilidades extraordinárias",         "o-1",  "comprovante de habilidades extraordinárias"),
    ("comércio",                            "e-1",  "provas comércio"),
    ("investimento",                        "e-2",  "provas investimento"),
    ("casamento",                           "k-1",  "processo de casamento"),
    ("serviço diplomático",                 "a-1",  "diploma diplomático"),
    ("serviço internacional embaixada",     "g-1",  "carta organização internacional"),
    ("serviço internacional governo",       "g-2",  "carta organização internacional"),
    ("serviço internacional representante", "g-3",  "carta organização internacional"),
    ("serviço internacional eua",           "g-4",  "carta organização internacional"),
    ("família serviço internacional",       "g-5",  "carta organização internacional"),
    ("trabalho religioso",                  "r-1",  "provas de afiliação religiosa"),
    ("vítima tráfico humano",               "t",    "provas vítima tráfico humano"),
    ("vítima de crime",                     "u",    "provas vítima de crime"),
    ("reunião familiar",                    "v",    "provas de relacionamento"),
    ("serviço de tripulação",               "d",    "licença tripulação"),
    ("membro da OTAN",                      "nato", "identificação OTAN"),
    ("status",                              "p-1",  "Documentação que comprove status de atleta ou artista de destaque"),
    ("NAFTA",                               "tn",   "None")
]

def verificar_embarque(tipo_de_visto: str, validade_visto: str, proposito_viagem: str, documentacao_suporte: str):
    for visto in vistos:
        if validade_visto == "válido":
            if proposito_viagem.lower() == visto[0].lower() and tipo_de_visto.lower() == visto[1].lower() and documentacao_suporte.lower() == visto[2].lower():
                print("Verificar documentação: ",visto[2].lower())
                return
    print("Restrições de visto ou documentação inadequada. Embarque não permitido.")


def return_age(date: d.datetime) -> int:
    today = d.datetime.now()
    # d.relativedelta faz a diferença considerando anos bissextos // d.relativedelta makes a difference considering leap years
    age = d.relativedelta(today, date).years
    return age

def check_validity(visa_validity: d.datetime) -> bool:
    today = d.datetime.now()
    return today > visa_validity


if __name__ == '__main__':
    # Testa a função verificar_embarque
    tipo_de_visto_passageiro = "B-1"
    validade_visto_passageiro = "válido"
    proposito_viagem_passageiro = "empregado domestico"
    documentacao_suporte_passageiro = "carta convite"
    verificar_embarque(tipo_de_visto_passageiro, validade_visto_passageiro, proposito_viagem_passageiro, documentacao_suporte_passageiro)

    # Testa a função return_age
    data_nascimento = d.datetime(1990, 5, 15) 
    idade = return_age(data_nascimento)
    print("A idade é:", idade, "anos")

    # Testa a função check_validity
    validade_visto = d.datetime(2023, 12, 31)
    validade_passada = check_validity(validade_visto)
    if validade_passada:
        print("A validade já passou.")
    else:
        print("A validade ainda não passou.")