#    TESTANDO O F-STRING

name = "John"

myString = "Hello, " + name + "."
myfString1 = f"Hello, {name}."
myfString2 = f"Hello, {name.upper()}."
myfString3 = f"How old are you: {10 + 8}."
myfString4 = f"O número 2 é maior que o número 1: {2 > 1}"
myfString5 = f"O número 2 está contido na lista [4, 5, 6]: {2 in [4, 5, 6]}"

print(myString)
print(myfString1)
print(myfString2)
print(myfString3)
print(myfString4)
print(myfString5)

#         USANDO OUTRAS FUNCIONALIDADES DE FORMATAÇÃO DE STRINGS
from datetime import datetime

frutas = ['Jaca', 'laranja', 'uva', 'banana']
for fruta in frutas:
    my_fruit = f"Nome: {fruta:12} - Número de letras: {len(fruta):3}"
    print(my_fruit)

print()

pi = 3.1415
myNumber = f'O número PI é: {pi:1f}'
myNumberdeslocado = f'O número PI deslocado é: {pi:6.1f}'
myNumberpreciso = f'O número PI mais preciso é: {pi:4f}'
print(myNumber)
print(myNumberdeslocado)
print(myNumberpreciso)

print()

data = datetime.now()
mydate = f'A data de hoje é {data}'
mydateformatted = f'A data de hoje formatada é {data:%d/%m/%y}'
print(mydate)
print(mydateformatted)

