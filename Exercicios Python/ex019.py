# Faça um programa em que um professor quer sortear um de seus quatro alunos para apagar o quadro. Ajude ele com o programa lendo o nome deles e escrevendo o nome do escolhido.

a1 = str(input("Digite o nome do primeiro aluno(1): "))
a2 = str(input("Digite o nome do segundo aluno(2): "))
a3 = str(input("Digite o nome do terceiro aluno(3): "))
a4 = str(input("Digite o nome do quarto aluno(4): "))

lista = [a1, a2, a3, a4]
import random
print("O aluno escolhido foi {}: ".format(random.choice(lista)))