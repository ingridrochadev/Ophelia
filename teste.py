from src.database.utils.utils_visto import Funcoes
from src.database.utils.utils_usuario import Sistema


instancia = Funcoes()
instancia2 = Sistema()

print(instancia2.buscar_usuario('ADM001'))
print(list(instancia.buscar_por_passaporte('ABC123456')))
