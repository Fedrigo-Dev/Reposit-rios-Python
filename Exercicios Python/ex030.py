# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = float(input("Digite o número a ser calculado: "))

if n % 2 == 0:
    print("O número {} é par!".format(n))
else:
    print("O número {} é impar!".format(n))
