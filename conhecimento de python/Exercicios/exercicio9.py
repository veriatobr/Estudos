''' Faça um programa que peça para digitar um numero inteiro e mostre seu antecessor e seu sucessor '''

numero = int(input("digite um numero: "))

antecessor = numero-1
sucessor = numero+1

print("numero digitado foi {}".format(numero))
print("e seu antecessor é: {}".format(antecessor))
print("e seu sucessor é: {}".format(sucessor))