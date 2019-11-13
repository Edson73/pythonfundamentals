# string = 'palavra' ou "palavra" ou 'numero' ou "numero"
# inteiro = 10 ou 15 ou -10 ou -15
# float = 1.50 ou 10.18 ou -1.5 ou -10.18 ou 10.00
# bool = True ou False

# s = True

# if s is True:
#     print('é True')
# else:
#     print('é False')

# strings
rua = 'vergueiro'
endereco = 'Rua Vergueiro 1057'
# print(rua[0])
# print(rua.upper())
# print(rua.lower())
# print(rua.capitalize()) somente a primeira letra maiuscula
# amazon = '1998,Acre,Janeiro,0,1998-01-01 \
# 1999,Acre,Janeiro,0,1999-01-01'
# amazon_list = amazon.split(',')
# print(endereco.split(' '))
# print(rua.islower())
# print(rua.isdecimal())

# listas
# listas podem guardar diferentes tipos de dados
lista_1 = [1, 2, 3, 'abacaxi', 'carro', 1.4, True]
print(lista_1[0]) # indexar lista
lista_1.append('casa') # adicionar coisas
lista_1.pop(0) # métodos precisam utilizar () # remover pelo index
lista_1.remove('carro') # remover
lista_1.sort() # colocar em ordem alfabetica
lista_1.sort(reverse=True) # ordem alfabetica ao contrario
lista_1.reverse() # inverter a lista

# tupla
tupla = (1, 2, 3, 4) # imutável
tupla = 1,2,3 # uma tupla
tupla.count(1) # contar itens dentro da tupla
tupla.index(0) # retorna o item do index
len(tupla) # conta o número de itens na tupla