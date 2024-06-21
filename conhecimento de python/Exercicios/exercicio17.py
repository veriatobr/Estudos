"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        salários até R$ 280,00 (incluindo) : aumento de 20%
        salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
        o salário antes do reajuste;
        o percentual de aumento aplicado;
        o valor do aumento;
        o novo salário, após o aumento."""

base = float(input("DIGITE UM SALARIO PARA CALCULO DE AUMENTO: R$"))
                    
aumento1 = base*20/100
aumento2 = base*15/100
aumento3 = base*10/100
aumento4 = base*5/100

salario1 = base+aumento1
salario2 = base+aumento2
salario3 = base+aumento3
salario4 = base+aumento4

if base <= 280:
    print(f"Seu salario antes do aumento era: R${base:.2f}, voce recebeu um aumento de 20% de aumento, valor esse de: R${aumento1:.2f} , ficando o total dos proximos vencimentos de: R${salario1:.2f}")
elif base >= 281 and base <= 700:
    print(f"Seu salario antes do aumento era: R${base:.2f}, voce recebeu um aumento de 15%, valor esse de: R${aumento2:.2f}, ficando o total dos proximos vencimentos de: R$ {salario2:.2f}")
elif base >= 700 and base <= 1500:
    print(f"Seu salario antes do aumento era: R${base:.2f}, voce recebeu um aumento de 10%, valor esse de: R${aumento3:.2f}, ficando o total dos proximos vencimentos de: R$ {salario3:.2f}")
elif base >= 1500:
    print(f"Seu salario antes do aumento era: R${base:.2f}, voce recebeu um aumento de 5%, valor esse de: R${aumento4:.2f}, ficando o total dos proximos vencimentos de: R$ {salario4:.2f}")
    
else:
    print("opcao invalida")