# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print("Olá, vamos conferir se você sofreu uma multa por excesso de velocidade?")
# Limite de veloidade 80km/h
limite = 80
v = float(input("Qual a velocidade atual do seu carro?(km/h) "))

if v < limite:
    print("Tenha um bom dia, dirija com cuidado!")
    print("-=-" * 20)
    print("--E NÃO SE ESQUEÇA, SE BEBER NÃO DIRIJA KRL!!!!!!!!!!!--")
    print("-=-" * 20)
else:
    multa = (v - limite) * 7
    print("Sua velocidade excedeu o limite permitido de 80km/h, terá que pagar a multa!")
    print("O valor que terá que pagar será: {:.2f}".format(multa))