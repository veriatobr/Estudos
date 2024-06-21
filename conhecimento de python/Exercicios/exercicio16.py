""" A  Telefonou para a vítima?
        B  Esteve no local do crime?
        C  Mora perto da vítima?
        D  Devia para a vítima?
        E  Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como Inocente.  """





  
local_crime = str(input("ESTEVE NO LOCAL DO CRIME ? "))
print("")
mora_perto = str(input("MORA PERTO DA VITIMA? "))
print("")
devia = str(input("DEVIA PARA A VITIMA? "))
print("")
trabalhou =  str(input("JA TRABALHOU COM A VITIMA? "))
print("")

print(f"{local_crime,mora_perto,devia,trabalhou}")

