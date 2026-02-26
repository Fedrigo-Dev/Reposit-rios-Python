r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))

modo1eq = False
modo2es = False
modo3iso = False
tri = False

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    tri = True
    print("É possível formar um triangulo")

    if r1 == r2 == r3:
        print("Pode formar um triângulo e é EQUILATERO!")
    elif r1 != r2 and r2 != r3 and r1 != 3:
        print("Pode formar um triângulo e é ESCALENO!")
    else:
        print("Pode formar um triângulo e é ISOCELES!")
else:
    print("Não pode formar um triângulo")