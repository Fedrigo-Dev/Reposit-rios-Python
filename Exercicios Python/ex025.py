# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

n = input("Digite seu nome: ").strip().upper()
print ("SILVA" in n.upper())
if "SILVA" in n:
    print("Seu nome contém SILVA... {}".format(n.upper()))
else:
    print("Seu nome não contém SILVA...")
