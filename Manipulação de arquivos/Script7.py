#         TESTANDO O MÉTODO SPLIT

#Criando uma frase atribuindo a uma variável
frase1 = "Hello world"
terms_list1 = frase1.split()
print(terms_list1)

#Criando a segunda frase com mais espaços em brancos
frase2 = "Hello  Mundo"
terms_list2 = frase2.split()
print(terms_list2)

#Criando a terceira frase colocando vírgulas
frase3 = "Hello,Mundo,Olá,World"
terms_list3 = frase3.split(',')
print(terms_list3)

#Fazedno uma contagem com o count e com o split
frase = "Eu amo comer cuzcuz no café da manhã"

#Método count
print("Contagem ditera: ", frase.count("amo"))

#Método split
contation = 0
terms_list = frase.split()
for termo in terms_list:
    if termo == 'amo':
        contation += 1
print("Contagem correta: ", contation)

#Usando os dois métodos
phrase = "quantos patos fazem quack"
list = phrase.split()
contator = list.count("qua")
print("Contagem = ", contator)