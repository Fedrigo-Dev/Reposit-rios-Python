
print ("Olá, vamos calcular? ")
print ("Quero que você digite os números que deseja. ")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))



print ("Agora vamos escolher a operação matemática que deseja fazer. ")
print ("Quer fazer qual opoeração matemática?(+,-,*,/)") 
operacao = input("Operação: ")
if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*":
    resultado = n1 * n2
elif operacao == "/":
    resultado = n1 / n2
elif operacao == "//":
    resultado = n1 // n2
elif operacao == "**":
    resultado = n1 ** n2
elif operacao == "%":
    resultado = n1 % n2
else:
    print("Operação inválida!")
    resultado = 0

print ("O resultado da operação realizada com os números {} e {} é: {}".format(n1, n2, resultado)) 