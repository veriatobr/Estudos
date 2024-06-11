'''
    Faça um programa que leia o valor de um produto e calcule o desconto dele de 5% e mostre o seu novo preço com 5% de desconto
'''

produto = float(input("valor do produto R$"))
desconto = float(input("digite a porcentagem do desconto"))
resultado = produto*desconto/100
valorfinal = produto-resultado

#print("Valor do produto{}".format(produto))
print("Desconto{} %".format(desconto))
print("Valor TOTAL DO PRODUTO {} Reais".format(valorfinal))


