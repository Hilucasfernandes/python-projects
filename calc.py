while True:
    try: # Pedir os números e verificar se são válidos
        number1 = float(input("Qual o primeiro número? "))
        number2 = float(input("Qual o segundo número? "))
    except ValueError:
        print("Formato inválido")
        continue
    
    operation = input("Qual operador você deseja (+ - * /)? ")
    print(f"[DEBUG] - Calculo desejado: {number1} {operation} {number2}")
    
    if operation == "+": # Verificar o operador escolhido e fazer o calculo
        calc = round(number1 + number2, 2)
        print(f"O calculo de {number1} + {number2} é {calc}")
    elif operation == "-":
        calc = round(number1 - number2, 2)
        print(f"O calculo de {number1} - {number2} é {calc}")
    elif operation == "*":
        calc = round(number1 * number2, 2)
        print(f"O calculo de {number1} * {number2} é {calc}")
    elif operation == "/":
        if number2 == 0: # Se caso o usuário tentar dividir o número por 0, o script irá falar que não é permitido
            print("Calculo inválido: Divisão por zero não é permitida.")
            print(f"[DEBUG]: Primeiro Número - {number1}, Segundo Número - {number2}")
        else:
            calc = round(number1 / number2, 2)
            print(f"O calculo de {number1} / {number2} é {calc}")
    else:
        print("Operação inválida")
        continue
    
    choose = input("Você deseja continuar? (s/n) ").lower()
    if choose != "s": # Verificar se o usuário quer continuar ou não
        print("Encerrando calculadora!")
        break
