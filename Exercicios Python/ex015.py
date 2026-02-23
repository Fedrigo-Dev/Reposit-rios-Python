km = float(input("Digite quantos km foram rodados: "))
dias = int(input("Digite quantos dias o carro foi alugado: "))
preço_km = km * 0.15
preço_dias = dias * 60
preço_total = preço_km + preço_dias
print("O preço total a pagar é: R$ {:.2f}".format(preço_total))