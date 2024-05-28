# Solicitando ao usuário que forneça os dados para o dicionário
dados_usuario = {}

print("Por favor, forneça os dados para o dicionário:")

chave1 = input("Chave 1: ")
valor1 = input("Valor correspondente à Chave 1: ")
dados_usuario[chave1] = valor1

chave2 = input("Chave 2: ")
valor2 = input("Valor correspondente à Chave 2: ")
dados_usuario[chave2] = valor2

chave3 = input("Chave 3: ")
valor3 = input("Valor correspondente à Chave 3: ")
dados_usuario[chave3] = valor3

chave4 = input("Chave 4: ")
valor4 = input("Valor correspondente à Chave 4: ")
dados_usuario[chave4] = valor4

# Exibindo o dicionário criado com os dados do usuário
print("\nDicionário criado com os dados informados pelo usuário:")
print(dados_usuario)