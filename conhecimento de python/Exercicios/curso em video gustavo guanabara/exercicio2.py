"""faca um programa que pergunte o dia , mes e ano de uma pessoa e depois formate a mensagem"""


nome = str(input("Qual seu nome? "))
dia = int(input("Que dia voce nasceu? "))
mes = str(input("Qual mes de nascimento? "))
ano = int(input("Qual ano de nascimento? "))


print(f"Seu nome é {nome} , voce nasceu no dia {dia} do mes de {mes} do ano de {ano}, correto? ")