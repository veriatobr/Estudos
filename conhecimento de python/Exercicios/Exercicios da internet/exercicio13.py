
"""Faça um programa que pergunte a idade e veja se a pessoa é criança de 1 até 9 anos, adolescente de 10 até 14 anos, jovem de 15 até 17, adulto de 18 até 64 e velho acima de 65"""


nome = int(input("Digite sua idade: "))

if nome >=1 and nome <=9:
    print("voce é uma crianca!")
elif nome >=10 and nome <=14:
    print("voce é adolescente!")
elif nome >=15 and nome <=17:
    print("voce é jovem!")
elif nome >=18 and nome <=64:
    print("voce é adulto!")
elif nome > 65:
    print("voce é idoso!")
    
else:
    print("opcao invalida")