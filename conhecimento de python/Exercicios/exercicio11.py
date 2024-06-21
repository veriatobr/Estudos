'''Crie um programa que leia o preço de um produto, e como forma de pagamento pergunte se é a vista ou parcelado. Se for a vista, ganha 12% de desconto. Se o produto for parcelado, 15% a mais de juros. E no crediário, taxa de 22% de juros. Depois mostre o total do produto com desconto ou com juros.'''

preco = float(input("QUAL PRECO DO PRODUTO? "))
formadepag = str(input("Pagamento a vista,Parcelado ou Crediario: "))
desconto = 12/100*preco
vista = preco-desconto
parcelado = preco*15/100+preco
crediario = preco*22/100+preco
#print("{:.0f}.00 Reais{:.0f}.00 Reais{:.0f}.00 Reais".format(vista,parcelado,crediario))

if formadepag == "a vista":
    print("Valor a vista R${:.2f}".format(vista))
    print("")
elif formadepag == "parcelado":
    print("Valor parcelado R${:.2f}".format(parcelado))
    print("")
elif formadepag == "crediario":
    print("Valor do produto no crediario R${:.2f}".format(crediario))
    print("")


    
    
    
    
   







