#   TESTANDO O MODO WRITELINE

#Criando as linhas do arquivo em forma de lista
linhas = ["Hello ",
          "\nWorld"]

#Abrindo o arquivo com o modo "w"
arquivo_escrito = open("Texto.txt", "w")
arquivo_escrito.writelines(linhas)

#fechando
arquivo_escrito.close()
print("Está fechado:", arquivo_escrito.closed)