from src.database.utils.utils_visto import Funcoes
from src.database.utils.utils_usuario import Sistema


instancia = Funcoes()
instancia2 = Sistema()

print(instancia2.buscar_usuario('ADM001'))
print(list(instancia.buscar_por_passaporte('ABC123456')))

nome, data_nascimento, nacionalidade, tipo_visto, numero_visto, data_validade, local_emissor, status = list(instancia.buscar_por_passaporte('ABC123456'))
data_nasc = data_nascimento.strftime("%d-%m-%Y")
data_validade_format = data_validade.strftime("%d-%m-%Y")

print(nome, data_nascimento, nacionalidade, tipo_visto, numero_visto, data_validade, local_emissor, status)