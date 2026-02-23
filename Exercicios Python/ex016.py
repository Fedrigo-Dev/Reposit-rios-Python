# Exercício 16: Crie um programa que leia a raiz quadrada de um número.

import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, math.trunc(num)))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
