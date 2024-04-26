from src.database.utils.utils_visto import Funcoes
from src.database.utils.utils_usuario import Sistema


instancia = Funcoes()
instancia2 = Sistema()

# print(instancia2.buscar_usuario('ADM001'))
# print(list(instancia.buscar_por_passaporte('ABC123456')))

# nome, data_nascimento, nacionalidade, tipo_visto, numero_visto, data_validade, local_emissor, status = list(instancia.buscar_por_passaporte('ABC123456'))
# data_nasc = data_nascimento.strftime("%d-%m-%Y")
# data_validade_format = data_validade.strftime("%d-%m-%Y")

# print(nome, data_nascimento, nacionalidade, tipo_visto, numero_visto, data_validade, local_emissor, status)

# print(instancia2.criar_usuario("Administrador", "46590518033", "admin@ophelia.com", "admin1@A", "ADM001", "Supervisor"))
# print(instancia2.criar_usuario("Usuário Normal", "82896051023", "user@ophelia.com", "user2@A", "USR001", "Agente de Aeroporto"))
# print(instancia2.criar_usuario("João Silva", "76454264033", "joao.silva@ophelia.com", "Senha123@", "USR002", "Agente de Aeroporto"))
# print(instancia2.criar_usuario("Ana Santos", "19975090087", "ana.santos@ophelia.com", "Senha456@", "USR003", "Supervisor"))
# print(instancia2.criar_usuario("Pedro Oliveira", "49368067066", "pedro.oliveira@ophelia.com", "Senha789@", "USR004", "Agente de Aeroporto"))
# print(instancia2.criar_usuario("Maria Pereira", "78512404094", "maria.pereira@ophelia.com", "Senha147@", "USR005", "Agente de Aeroporto"))
# print(instancia2.criar_usuario("Carlos Ferreira", "62183463074", "carlos.ferreira@ophelia.com", "Senha258@", "USR006", "Agente de Aeroporto"))
# print(instancia2.criar_usuario("Eduardo Souza", "65004417024", "eduardo.souza@ophelia.com", "Senha369@", "USR007", "Agente de Aeroporto"))


print(instancia2.excluir_usuario("34275428072"))