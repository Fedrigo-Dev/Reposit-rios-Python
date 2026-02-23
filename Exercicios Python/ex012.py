preço = float(input("Digite o preço do produto: "))
desconto = preço * 0.05
preço_com_desconto = preço - desconto
print("O preço do produto com desconto é: R$ {:.2f}".format(preço_com_desconto))