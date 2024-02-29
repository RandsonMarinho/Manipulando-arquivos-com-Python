#      LIDANDO COM EXCEÇÕES
print("Opening archive")

#Tentativa de executar algo no código
try:
    open("Texto.txt", "w")
    print("Arquivo aberto!")

#Caminho alternativo caso dê alguma bosta
except FileNotFoundError as erro:
   print("Arquivo não existe")
   print("Descrição", erro)

print("Término do programa")
