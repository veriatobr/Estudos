'''
    Faça um programa que pergunte o valor de um  numero e calcule sua raiz quadrada
    
'''

import math
#formula raiz quadrada n**(1/2)
valor = float(input("Digite um numero:"))
raiz1 = valor**(1/2)

print("A Raiz Quadrada de {:.0f} é {}".format(valor,raiz1))

raiz2 = math.sqrt(valor)
print("A Raiz quadrada de {:.0f} é {}".format(valor,raiz2))


#{:} significa que vai puxar algo
#{.} significa que vai indicar que é um ponto flutuante (float)
#{2} significa a quantidade de casas decimais que você quer mostrar
#{f} faz referência ao float(tipo primitivo)