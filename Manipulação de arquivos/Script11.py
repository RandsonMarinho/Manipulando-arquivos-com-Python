#    TESATANDO O MÉTODO REMOVE
import os

try:
    with os.remove("texge.pdf") as arquivo:
       print("Arquivo não existe")
except FileNotFoundError as erro:
    print("Não encontrado")
    print("Esse foi o erro: ", erro)

print("Término do programa")


#    TESTANDO O MÉTODO RENAME
print("testando rename")

try:
    os.rename("testezinn.txt", "Texto.txt")
    print("funcionou")
except FileNotFoundError as erro:
    print("Deu erro")
    print("O erro foi: ", erro)
except FileExistsError as erro:
    print("arquivo já existe")
    print("erro: ", erro)