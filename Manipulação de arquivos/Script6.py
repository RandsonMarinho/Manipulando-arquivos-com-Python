#          TESTANDO O MÉTODO COUNT

#abrindo o arquivo com o with
with open("produtos.csv") as arquivo:
    content = arquivo.read()
    contation = content.count("Mouse")

#Exibindo a quantidade em que a palavra "Mouse" se repete
print("Total de Mouses:", contation)