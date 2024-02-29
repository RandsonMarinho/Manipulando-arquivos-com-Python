#        TESTANDO O MÉTODO STRIP

#Abrindo o arquvo com a função with
with open("produtos.csv") as arquivo:
    for linha in arquivo:
        clean_line = linha.strip()
        print(repr(clean_line))