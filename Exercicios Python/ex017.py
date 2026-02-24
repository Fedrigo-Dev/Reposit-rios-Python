# Faça um programa que leia o comrpimento do carero oposto e do cateto adjacente de um triâncuglo retângulo, calcule e mostre o comprimento da hipotenusa.

print("Olá, vamos calcular o comprimento da hipotenusa de um triângulo retângulo?")

from math import hypot

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(co, ca)
print ("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))
