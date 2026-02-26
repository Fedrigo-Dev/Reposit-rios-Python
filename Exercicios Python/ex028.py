# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

n = random.randint(0, 100)

print("-----Pensei em um número de 0 a 100, tente adivinhar!-----")

acertou = False

while not acertou:
    ne = int(input("Qual é o seu palpite? "))

    if ne == n:
        print("Você acertou o número!")
        acertou = True
    else:
        if ne < n:
            print("O número é maior, tente novamente: ")
        else:
            print("O número é menor, tente novamente: ")
print("-----Fim do jogo! o número que eu pensei foi: {}-----".format(n))
 