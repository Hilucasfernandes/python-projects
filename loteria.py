import random

numeros = []
numeros2 = []
acertos = 0

# Lógica para criar a lista com os números que o usuário escolheu
for i in range(5):
    while True:
        try:
            number = int(input(f"Digite o {i+1}º número (1 a 10): "))
            if 1 <= number <= 10:  # Verifica se o número está entre 1 e 10
                numeros.append(number)
                break
            else:
                print("Por favor, insira um número entre 1 e 10!")
        except ValueError:
            print("Por favor insira um número inteiro válido!")

# Lógica para criar a lista com os números que a máquina escolheu
for ii in range(5):
    number2 = random.randint(1, 10)
    numeros2.append(number2)

# Lógica que compara os números e verifica se o usuário acertou
print("\nComparação dos números:")
for iii in range(5):
    if numeros[iii] == numeros2[iii]:
        print(f"O número {iii+1} acertou! ({numeros[iii]} == {numeros2[iii]})")
        acertos += 1
    else:
        print(f"Errou o número {iii+1}! ({numeros[iii]} != {numeros2[iii]})")

# Exibe os números e a quantidade de acertos
print("\nNúmeros inseridos:", numeros)
print("Números aleatórios:", numeros2)
print("\nVocê acertou:", acertos, "número(s).")

# Condicional baseada na quantidade de acertos
if acertos == 5:
    print("Parabéns, você acertou todos os números!")
elif acertos >= 3:
    print("Muito bem! Você acertou uma boa quantidade de números.")
else:
    print("Você acertou poucos números, tente novamente!")
