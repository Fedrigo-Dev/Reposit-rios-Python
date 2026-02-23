n1 = float(input("Sua nota na primeira avaliação foi: "))
n2 = float(input("Sua nota na segunda avaliação foi: "))
media = (n1 + n2) / 2
print("A sua média é: {}".format(media))
if media >= 7:
    print("Parabéns, você foi aprovado!")
elif media >= 5:
    print("Você está de recuperação!")
else:
    print("Infelizmente, você foi reprovado, energumeno, merece comer alface na cadeia, animal, acéfalo, infeliz, mal amado.")