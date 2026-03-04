while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break  # sai do loop se a conversão funcionar
    except ValueError:
        print("Entrada inválida! Você precisa digitar um número inteiro.")

# Verifica se é par ou ímpar
if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")