# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))

modo1eq = False
modo2es = False
modo3iso = False
tri = False

if tri == (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("Pode formar um triangulo!")
    tri = True
elif tri == (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2) and modo1eq == (r1 == r2) and (r2 == r3):
    tri = True
    modo1eq = True
    print("Pode formar um triangulo!")
    print("O triangulo é equilatero!")
elif tri == (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2) and modo2es == (r1 != r2) and (r2 != r3) and (r1 != r3):
    tri = True
    modo2es = True
    print("Pode formar um triangulo!")
    print("O triangulo é escaleno!")
elif tri == (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2) modo3iso == (r1 == r2) and (r1 != r3) and (r1 == r3) and (r1 != r2):
    tri = True
    modo3iso = True
    print("Pode formar um triangulo!")
    print("O triangulo é isóceles!")


