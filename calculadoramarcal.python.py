print("===bem-vindo à calculadora do marçalx===")
num1 = float(input ("Digite o primeiro número: "))
num2 = float(input ("Digite o segundo número: "))
print("Escolha a operação desejada:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = input("Digite o número da operação desejada (1/2/3/4): ")

if opcao == "1":
    print("A soma dos números é: " + str(num1 + num2))
elif opcao == "2":
    print("A subtração dos números é: " + str(num1 - num2))
elif opcao == "3":
    print("A multiplicação dos números é: " + str(num1 * num2))
elif opcao == "4":
    print("A divisão dos números é: " + str(num1 / num2))
else:
    print("Opção inválida. Por favor, escolha uma operação válida.") 
while True:
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == "s":
        num1 = float(input ("Digite o primeiro número: "))
        num2 = float(input ("Digite o segundo número: "))
        print("Escolha a operação desejada:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        opcao = input("Digite o número da operação desejada (1/2/3/4): ")

        if opcao == "1":
            print("A soma dos números é: " + str(num1 + num2))
        elif opcao == "2":
            print("A subtração dos números é: " + str(num1 - num2))
        elif opcao == "3":
            print("A multiplicação dos números é: " + str(num1 * num2))
        elif opcao == "4":
            print("A divisão dos números é: " + str(num1 / num2))
        else:
            print("Opção inválida. Por favor, escolha uma operação válida.")
    elif continuar.lower() == "n":
        print("Obrigado por usar a calculadora do marçalx. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")