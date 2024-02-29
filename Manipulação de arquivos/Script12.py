#    CRIADNO E REMOVENDO DIRETÓRIOS
import os

try:
    os.mkdir("my_directory")
    print("Diretório criado com sucesso")
except PermissionError as erro:
    print("Sem permissão")
except FileExistsError as erro:
    print("O arquivo já existe")

print("Encerrado")

print("Removendo diretório")

try:
    os.rmdir("my_directory")
    print("Diretório removido")
except PermissionError as erro:
    print("Não permitido")
except FileNotFoundError as erro:
    print("Não encontrado")

except OSError as erro:
    print("Erro")
    print("Diretório não está vazio")
    print("Erro: ", erro)

print("Encerrado")
