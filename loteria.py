import random

numeros = []
numeros2 = []

for i in range(5): # Lógica que faz uma lista com os números que o usuário escolheu
    while True:
        try:
            number = int(input(f"Digite o {i+1} "))
            numeros.append(number)
        except ValueError: # Se caso ele não der um número inteiro válido retornar uma mensagem
            print("Por favor insira um número inteiro válido!")

for ii in range(5): # Lógica que faz uma lista com os números que a máquina escolher
    number2 = random.randint(1, 10)
    numeros2.append(number2)

for iii in range(5): # Lógica que compara os números e verifica se o usuário acertou
    if numeros[iii] == numeros2[iii]:
        print(f"O número {iii+1} acertou! ({numeros[iii]} == {numeros2[iii]})")
    else:
        print(f"Errou o número {iii+1}! ({numeros[iii]} != {numeros2[iii]})")
        
print("\nNúmeros inseridos:", numeros)
print("Números aleatórios:", numeros2)