import random

tentativas = 0

while True:
    try:
        resposta = int(input("Qual seu chute (Número de 1 a 10): "))
        print(f"[DEBUG]: Usuário selecionou um número com sucesso!")
    except ValueError:
        print(f"[ERROR]: O que você digitou não está no formato do jogo!")
        continue  # Volta ao início do loop para pedir novamente a entrada do usuário
    
    if resposta < 1 or resposta > 10:
        print("Número fora do intervalo permitido! Escolha um número entre 1 e 10.")
        continue  # Volta ao início para pedir um número válido

    tentativas += 1
    correta = random.randint(1, 10)
    
    if resposta == correta:
        print("Acertou!")
        print(f"Número correto: {correta}")
        print(f"Você acertou em {tentativas} tentativa(s)!")
        break  # Sai do loop ao acertar
    else:
        print("Errou!")
        print(f"Número escolhido: {resposta}")
        print(f"Número correto: {correta}")
