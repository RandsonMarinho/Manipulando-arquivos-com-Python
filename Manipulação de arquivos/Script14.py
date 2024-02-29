#   TESTANDO O MÉTODO SCANDIR PARA SCANEAR UM DIRETÓRIO QUALQUER

import os

try:
    entradas = os.scandir("my_directory")

    for i in entradas:
        print(i)

except FileNotFoundError as erro:
    print("Caminho nao existe")
    print(erro)
except NotADirectoryError as erro:
    print("O caminho não é de um diretório")
    print(erro)