"""faca uma simulacao de financiamento de veiculo , descubra o valor aproximado que ficara a parcela e o valor final do financiamento com ou sem entrada."""

nome = str(input("DIGITE SEU NOME: "))
salario = float(input("DIGITE SEU SALARIO:R$"))
valorveiculo = float(input("DIGITE O VALOR DO VEICULO DESEJADO:R$"))
entradasimounao = str(input("DESEJA DAR ENTRADA? "))
investimento1= float(input("VALOR DA ENTRADA:"))
taxajurospercentagem1 = float((input('Taxa de Juros (em %) :')))
taxajuro1=taxajurospercentagem1/100
anos1 = int(input('Anos:'))
varfuturo1= investimento1*pow(1+taxajuro1,3)
jurototal1 = investimento1*(pow(1+taxajuro1,3)-1)
print('\n\n\t\t O valor futuro é de {:.2f}'.format(varfuturo1))
print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal1))



"""parcelacomentrada = valorveiculo
valorcomentrada

parcelasementrada
valorsementrada


investimento1 = float((input('\n\nInvestimento Inicial:')))
taxajurospercentagem1 = float((input('Taxa de Juros (em %) :')))
taxajuro1=tjurospercentagem1/100
anos1 = int(input('Anos:'))
varfuturo1= investimento1*pow(1+tjuro1,3)
jurototal1 = investimento1*(pow(1+tjuro1,3)-1)
   print('\n\n\t\t O valor futuro é de {:.2f}'.format(varfuturo1))
   print('\n\t\t Os juros totais é de {:.2f}'.format(jurototal1))"""