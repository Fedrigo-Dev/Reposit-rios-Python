# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

a1 = str(input("Digite o nome do primeiro aluno(1): "))
a2 = str(input("Digite o nome do segundo aluno(2): "))
a3 = str(input("Digite o nome do terceiro aluno(3): "))
a4 = str(input("Digite o nome do quarto aluno(4): "))

lista = [a1, a2, a3, a4]
import random
random.shuffle(lista)
print("A ordem escolhida foi {}: ".format(lista))