# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = input("Digite seu nome: ").upper()
ndividido = n.split()
print("Seu nome completo é: {}".format(n))
print("Seu primeiro nome é: {}".format(ndividido[0]))
print("Seu último nome é: {}".format(ndividido[-1]))
