# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

n = input("Digite uma frase:").upper()

print("A letra A aparece {} vezes na frase.".format(n.count('A')))
print("A primeira letra A apareceu na posição: {}".format(n.find('A')))
print("A última letra A apareceu na posição: {}".format(n.rfind('A')+1))
