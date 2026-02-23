largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite o comprimento da parede: "))
area = largura * altura
print("A área da parede é: {}m²".format(area))
tinta = area / 2
print("A quantidade de tinta necessária para pintar a parede é: {} litros".format(tinta * 2))
