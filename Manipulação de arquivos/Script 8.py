#        TESTANDO O MÉTODO JOIN

#Criando a lista com os conteúdos da frase
myList = ["Rice", "Bean", "Pasta"]

tex1 = ', '.join(myList)

#Abrindo o arquivo no modo w
with open("Texto.txt", "w") as archive:
    archive.write(tex1)

#Fazendo junção de elemntos de mesma linha
tex2 = '\n'.join(myList)
with open("produtos.csv", "w") as arquivo:
    arquivo.write(tex2)

