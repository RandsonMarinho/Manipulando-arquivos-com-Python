#      Contando a quantidade de linhas de um arquivo

#Abrindo o arquivo com a função with
with open("produtos.csv") as arquvio:

#Criadndo a variável contation e para cada linha que tiver algo escrito no arquivo o contation aumenta 1
    contation = 0
    for line in arquvio:
        if line:
           contation += 1

#Exibindo o resultado final
print("Total de linhas do arquivo", contation)