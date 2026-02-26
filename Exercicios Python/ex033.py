# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n = int(input("Digite o primerio valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
lista = [n, n2, n3]
maior = lista
menor = lista

if n > n2 and n > n3:
     maior = n
     print("-+-" * 10)
     print ("O maior número é: {}".format(maior))
     print("-+-" * 10)
else:
     if n2 > n and n2 > n3:
        maior = n2
        print("-+-" * 10)
        print ("O maior número é: {}".format(maior))
        print("-+-" * 10)
     else:
        if n3 > n and n3 > n2:
            maior = n3
            print("-+-" * 10)
            print ("O maior número é: {}".format(maior))
            print("-+-" * 10)



if n < n2 and n < n3:
    menor = n
    print("---" * 10)
    print("O menor número é: {}".format(menor))
    print("---" * 10)
else:
    if n2 < n and n2 < n3:
        menor = n2
        print("---" * 10)
        print("O menor número é: {}".format(menor))
        print("---" * 10)
    else:
        if n3 < n and n3 < n2:
            menor = n3
            print("---" * 10)
            print("O menor número é: {}".format(menor))
            print("---" * 10)

if n == n2 and n == n3:
    print("===" * 16)
    print("O números são iguais, não tem menor nemm maior...")
    print("===" * 16)
