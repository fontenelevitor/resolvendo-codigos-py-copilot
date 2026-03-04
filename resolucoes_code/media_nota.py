notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Digite a nota {i+1}: "))
            if nota < 0:
                print("Erro: a nota não pode ser negativa. Tente novamente.")
            else:
                notas.append(nota)
                break  # sai do loop se a nota for válida
        except ValueError:
            print("Entrada inválida! Você precisa digitar um número.")

# Calcula a média
media = sum(notas) / len(notas)

# Exibe o resultado
print(f"A média das notas é {media:.2f}")