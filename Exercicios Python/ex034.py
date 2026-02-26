# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salário: "))

if salario > 1250:
    aumento = salario * 0.10
    salarior = salario + aumento
    print("-+-" * 20)
    print("Seu salário recondicionado fica com o total de: R${:.2f}".format(salarior))
    print("-+-" * 20)
else:
    if salario <= 1250:
        aumentoamenos = salario * 0.15
        salarior = salario + aumentoamenos
        print("---" * 20)
        print("Seu salário recondicionado fica com o total de: R${:.2f}".format(salarior))
        print("---" * 20)
