# Crie um programa que leia o nome completo de uma pessoa e mostre o nome com todas as letras maiúsculas e minúsculas, quantas letras ao todo(sem considerar espaços)

n = input("Digite seu nome: ")
n1 = n.split()

print("Seu nome com letras maiúsculas é {} ".format(n.upper()))
print("Seu nome com letras minúsculas é {} ".format(n.lower()))
print ("A quantidade de letras que tem no seu nome é", len(n.replace(" ", "")))
print("O primeiro nome tem exatas", len(n1[0]))