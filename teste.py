from src.database.utils.utils_visto import Funcoes
from src.database.utils.utils_usuario import Sistema


instancia = Funcoes()
instancia2 = Sistema()
# print(instancia.verificar_regras_embarque('F1', '25-04-1993', '30-05-2032' ))
# print(instancia2.verificar_tipo_perfil('user@email.com'))

# print(instancia.listar_vistos())
# print(instancia.listar_vistos_sys())

# pyside6-uic cadastro.ui -o ui_main.py
# pyside6-rcc logo_.qrc -o logo_rc.py
# pyside6-uic login.ui -o ui_login.py

# perfil, nome = instancia2.verificar_tipo_e_nome_perfil('user@email.com')
# print(perfil, nome)

def listas(funcao):
    lista = funcao()
    print(lista)

# listas(instancia.listar_vistos_asc)
listas(instancia2.listar_usuarios_default)
listas(instancia2.listar_usuarios_asc)
listas(instancia2.listar_usuarios_desc)
# listas(instancia2.listar_usuarios_supervisor)
# listas(instancia2.listar_usuarios_supervisor_asc)
# listas(instancia2.listar_usuarios_supervisor_desc)
# listas(instancia2.listar_usuarios_agente)
# listas(instancia2.listar_usuarios_agente_asc)
# listas(instancia2.listar_usuarios_agente_desc)

# instancia2.enviar_confirmacao("ingridsigaa@gmail.com")



