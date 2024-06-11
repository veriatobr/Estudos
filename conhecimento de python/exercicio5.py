'''
    Peça para o usuario digitar o nome do aluno e digitar 2 notas do aluno e calcular a media
'''

nome = str(input("nome do aluno: "))
print("")
nota1 = float(input("primeira nota do aluno: "))
print("")
nota2 = float(input("segunda nota do aluno: "))
print("")
media = nota1+nota2/2

if nota1 <= 5:
    print("repetiu de ano")
    
else:
    print("passou de ano")

print("O aluno: {}".format(nome))
print("Teve no primeiro bimestre Nota: {}".format(nota1))
print("Teve no segundo  bimestre Nota: {}".format(nota2))
print("Media do semestre: {} ".format(media))

