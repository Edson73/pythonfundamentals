# -*- coding: utf-8 -*-

# Funções

# def mostraMaiorvalor(*valores):
#     print(max(valores))

# mostraMaiorvalor(1,2,62,73,58,59,9,745,9567,956)


# lista = []

# def listar():
#     global lista
#     print(lista)

# def adiciona(valor):
#     global lista  # tem que usar global para alterar lista dentro da função
#     return lista.append(valor)

# def remove(valor):
#     global lista
#     return lista.remove(valor)

# adiciona('Abacaxi')
# adiciona('Melão')
# adiciona('Caju')

# listar ()


# LAMBDA 3 funções: map, filter e reduce

# def subtrair(x, y):
#     '''subtrai valroes'''
#     retur x - y

# sub = lambda x, y: x - y # parametros: o que vai acontecer



# carrinho =[{"nome": "Tenis", "valor":21.70}, {"nome": "Camiseta", "valor":10.33}]

# black_friday = lambda x: x / 2

# for c in carrinho:
#     print(f'Nome do produto: {c["nome"]}')
#     print(f'Valor original: {c["valor"]}')
#     print(f'Valor com desconto: {black_friday(c["valor"])}')
#     print('=-'* 11)



# import pandas as pd

# itens = pd.read_csv('../arquivos/salarios.csv', usecols=['Name'])
# var = itens['Name']

# for c in var:

#     print(c)

# anonimas = [lambda x: x** 2, lambda x: x**3, lambda x: x** 4]

# for i in anonimas:
#     print(i(10))