from Ophelia.src.database.utils.utils_visto import Funcoes
from Ophelia.src.database.utils.utils_usuario import Sistema

instancia = Funcoes()
instancia2 = Sistema()
# print(instancia.verificar_regras_embarque('F1', '25-04-1993', '30-05-2032' ))
# print(instancia2.verificar_tipo_perfil('user@email.com'))

print(instancia.listar_vistos())
print(instancia.listar_vistos_sys())