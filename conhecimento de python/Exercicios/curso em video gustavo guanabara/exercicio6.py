"""crie um algoritimo que leia um numero e mostre o seui dobro , o triplo , e a raiz quadrada"""

from math import sqrt


num = int(input("Digite um numero: "))
#dobro = num*2
#triplo = num*3
#raiz = sqrt(num)

print(f" o numero escolhido é:{num}\n o dobro do numero escolhido é: {num*2}\n o triplo do numero escolhido é: {num*3}\n a raiz do numero escolhido é: {sqrt(num):.0f} ")