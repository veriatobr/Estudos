'''Crie um programa que pergunte a data de nascimento do usuário e veja qual a idade que ele tem na data atual'''

nascimento = int(input("Qual data do seu nascimento? "))
anoatual = 2024
idade = anoatual-nascimento

print("sua idade atual é: {} anos.".format(idade))