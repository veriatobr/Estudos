"""Faça um programa que pergunte a idade e veja se a pessoa é criança até 9 anos, adolescente até 14 anos, jovem até 17, adulto acima de 18 e velho acima de 65"""




idade = int(input("Qual sua idade?"))
if idade <= 9:
    print("Entao voce é crianca")
elif idade <= 14 and idade <17:
    print("entao voce é adolescente")
elif idade <= 17 and idade < 18:
    print("entao voce é jovem")
elif idade > 18 and idade < 65:
    print("entao voce é adulto")
elif idade > 65 and idade < 200:
    print("entao voce é velho")
else: 
    print("opcao invalida")
    
