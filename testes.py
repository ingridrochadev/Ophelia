# import uuid

# def generate_numeric_uuid4():
#     # Gera um UUID4 padrão
#     uuid_str = str(uuid.uuid4())
#     print(uuid_str)
#     # Remove os hífens e retorna apenas os números
#     return ''.join(c for c in uuid_str if c.isdigit())

# # Exemplo de uso:
# numeric_uuid = generate_numeric_uuid4()
# print("UUID4 Numérico:", numeric_uuid)


# nome = "Julia"
# print(nome[:3])
# nome[0] = J
# nome[1] = u
# nome[0] = J
# nome[0] = J
# nome[0] = and

# lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista2 = [2, 4, 6, 8, 10]

lista1 = []
lista2 = []

num = None
num2 = None

while num != 0:
    if num == 0:
        break
    num = int(input("Informe um número da primeira lista: "))
    lista1.append(num)
    
while num2 != 0:
    if num2 == 0:
        break
    num2 = int(input("Agora informe um número da segunda lista: "))
    lista2.append(num2)

for i in lista1:
    for j in lista2:
        if i == j:
            print(j)
            
print(lista1)
print(lista2)
