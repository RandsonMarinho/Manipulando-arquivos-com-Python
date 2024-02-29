#      TESTANDO O MODO APPEND

#abrindo o arquivo com o modo "a"(append)
arquivo_escrito = open("produtos.csv", 'a')

#Escrevendo em cima do arquivo ja existente
arquivo_escrito.write("\nEncerrado")

