#!/usr/bin/python3

# while
# x = 1
# while x < 10:
#     x += 1
#     print(f"numero: {x}")
# print('0 while acabou!')

# a = 500
# while a > 10:
#     print(a)
#     a -= 10

# while adicionando valores em uma lista
# x = 1
# lista = []
# while x < 1000:
#     lista.append(x
#     print(lista)
#     x += 1

# for
# fruta = ["Laranja", "Melancia", "Uva"]
# for f in fruta:
#     print(f)

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for var in l:
#     print(var)

# para printar o index junto
# frutas = ['abacaxi', 'banana', 'pera', 'maca', 'ameixa']
# for num, fruta in enumerate(frutas):
#     print(num, fruta)

# utilizando o for com a função range(inicio, fim, incremento)
# for item in range(10, 1, -1):
#     print(item)

# cont = 0
# while cont < 10:
#     print(f'vezes de execução {cont + 1}')
#     if cont == 2:
#         print('bloco de condição que interrompe o loop')
#         break
#     cont += 1

# t = 0
# while t < 10:
#     print(t)
#     if t == 5:
#         continue
#     t += 1

# Erros e Exceções
# try:
#     if 'Mariana' == nome:
#         print('nome correto')
#     else:
#         print('nome errado')
# except Exception as e:
#     nome = 'mariana'
# finally:
#     print(nome)

# try:
#     x = int(input('digite o primeiro numero: '))
#     y = int(input('digita o segundo numero: '))
#     print(x + y)
# except ValueError as t:
#     print('esse é um erro', t)

# while True:
#     try:
#         idade = int(input('Digite sua idade: '))
#         if idade < 16:
#             print('Você não pode comprar bebida alcolica e nem tirar titulo de eleitor')
#             break
#         else:
#             if idade >= 16 and idade < 18:
#                 print('Você pode ter um título de eleitor')
#                 break
#             else:
#                 print('Você pode comprar bebida e ter título de eleitor')
#                 break
#             break
#     except Exception as e:
#         print('Isso não é um número', e)
#         continue

# Raise Exception >> forçar um tipo de erro
# while True:
#     try:
#         login = input('Digite o login: ')
#         if login.lower() == 'bryan':
#             raise NameError('Bryan está banido!')
#         else:
#             print(f'Bem vindo {login}, acesso permitido!')
#             break
#     except NameError as e:
#         print(e)
#         continue

# try: >> tentar
#     x = int(input('Digite o primeiro número: '))
#     y = int(input('Digite o segundo número: '))
#     print(x + y)

# except ValueError as e: >> exceção
#     print('Digite apenas números,', e)

# while True: >> enquanto verdade
#     try:
#         x = int(input('Digite o primeiro número: '))
#         y = int(input('Digite o segundo número: '))
#         print(x + y)
#         break
#     except Exception as e:
#         print('Digite apenas números')
#         continue

# while True:
#     try:
#         user = input('Digite o nome de usuario: ')
#         if user == 'ana':
#             raise NameError('Usuario bloqueado!!')
#         else:
#             print(f'Bem vindo(a)')
#             break
#     except NameError as n:
#         print(n)
#         continue

# try:
#     login = input('Digite seu login: ')
#     if login == 'caio':
#         raise NameError('Usuario banido!')
#     else:
#         print(f'Bem vindo(a) {login}!')
# except NameError as n:
#     print(n)

