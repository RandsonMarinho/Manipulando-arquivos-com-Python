#    TESTANDO O MODO WRITE

#       Abrindo o arquivo de texto, atribuindo a uma variável e colocando no modo "w"(Write)
arquivo_escrita = open("Texto.txt", "w")

#       escrevendo a primeira linha no arquivo
arquivo_escrita.write("Hello")

#       escrevendo a segunda linha do arquivo; OBS: "\n" serve para pular uma linha
arquivo_escrita.write("\nWorld")

#fechando
arquivo_escrita.close()
print("Está fechado:", arquivo_escrita.closed)