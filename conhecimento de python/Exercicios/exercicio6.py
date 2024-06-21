'''
    Faça um programa que pergunte o valor em graus para o usuario e converta 1 para fahrenheit e outro para 2 para kelvin
    
    fahrenheit = float(input("Valor Graus Fahrenheit"))
kelvin = float(input("Valor Graus kelvin"))
'''



Celsius = float(input("Digite o valor em Graus celsius: "))


kelvin = Celsius+273.15 
fahrenheit = Celsius*1.8+32

print("A temperatura em Kelvin {}".format(kelvin))
print("A temperatura em Fahrenheit {}".format(fahrenheit))

