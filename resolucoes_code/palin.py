# Recebe a palavra do usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra
invertida = palavra[::-1]

# Verifica se é palíndromo
if palavra == invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
