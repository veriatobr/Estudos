"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato"""


preco1 = float(input("preco do primeiro produto: "))
preco2 = float(input("preco do segundo produto: "))
preco3 = float(input("preco do terceiro produto: "))

if preco1 > preco2 and preco1 > preco3:
    print("hahahah")
elif preco2 > preco1 and preco2 < preco3:
    print("ehuueheuhe")