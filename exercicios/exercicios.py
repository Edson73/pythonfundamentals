#!/usr/bin/python3

# Faça um programa que peça e imprima esse numero

# print(int(input('Digite um numero: ')))

# Faça um programa que receba 'F' ou 'M' e mostre Feminino ou Masculino

# Sexo = str(input('Digite o sexo: '))
# Sexo = Sexo.capitalize()

# if Sexo == 'F':
#     print('Feminino')

# elif Sexo == 'M':
#     print('Masculino')

# else:
#     print('Valor Invalido')

# Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo


# numero = int(input('Digite o numero: '))
# if numero > 0:
#     print('positivo')
# else:
#     print('negativo')

# Dada a lista ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']
# print 3, 13, Vasco
# print 5, São Paulo, 14
# mudem o valor do 4 para 30
# mudem o valor do 10 para 100
# mudem o valor do 14 para 150
# mudem o valor do Vasco para Bragantino

# lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14], 'Flamengo', 'Vasco']
# print(lista[1][2], lista[4][3], lista[6]) 
# print(lista[1][4], lista[3], lista[4][4])
# lista[4][0] = 100
# print(lista)
# lista[4][4] = 150
# print(lista)
# lista[6] = 'Bragantino'
# print(lista)
# lista[1][3] = 30
# print(lista)

# Dicionario
dados = {
    'cidades': {
        'saopaulo': {
            'nome': 'São Paulo',
            'municipios': 645,
            'populacao': 12.18
        },
        'riodejaneiro': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'populacao': 6.32
        },
        'minasgerais': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'populacao': 20.87
        }
    }

}
# print a quantidade de municipios de minas
# print(dados['cidades']['minasgerais']['municipios'])
# print a quantidade de municipios do rio
# print(dados['cidades']['riodejaneiro']['municipios'])
# print a populacao de minas em milhoes
# print(dados['cidades']['minasgerais']['populacao'] * 1000000)
# print a populacao de sao paulo em milhoes
# print(dados['cidades']['saopaulo']['populacao'] * 1000000)
# print o nome de sao paulo
# print(dados['cidades']['saopaulo']['nome'])

# conversão de tipos
# var = 15
# dada a variavel var, peça que o usuario digite um numero e multiplique por var
# var = 15
# print(int(input('Digite um valor: '))* var)

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada \
# por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez
# nome_aluno = input('Digite o nome do aluno: ')
# nota1 = float(input('Digite a primeira nota: '))
# nota2 = float(input('Digite a segunda nota: '))
# media_semestre = (nota1 + nota2)/2
# print(f'A nota do aluno {nome_aluno} é {media_semestre}')
# if media_semestre == 10.0:
#     print(f'Aluno {nome_aluno} for aprovado com distinção!')
# elif media_semestre >= 7.0 and media_semestre < 10.0:
#     print(f'Aluno {nome_aluno} foi aprovado!')
# else:
#     print(f'Aluno {nome_aluno} foi reprovado!')

#1 Faça uma lista com 10 usuários
#2 Peça para o usuário digitar o nome de usuário
#3 Caso não exista esse usuario na lista
#4 Dê um NameERROR volte para a parte 2
# usuarios = ['luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'pedro', 'fabricio']
# while True:
#     try:
#         login = input('Digite o nome de usuario: ')
#         if login.lower() not in usuarios:
#             raise NameError ('Usuário não existe.')
#         else:
#             print(f'Bem vindo(a) {login}!')
#             break
#     except NameError as n:
#         print(n)

# criar uma função que pega o conteudo da variavel texto
# e deixa em caixa alta
# texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'
# def upperTexto(text):
#     return text.upper()

# print(upperTexto(texto))


# Crie uma função que peça 2 números e retorne o maior
# se o valor for igual print "valores iguais"
# guarde uma variável e print

# def nMaior(x, y):
#     if x == y:
#         return 'valores iguais'
#     else:
#         return max(x, y)

# var = nMaior(12,12)
# print(var)



# Crie uma função que receba um número indefinido de valores numéricos
# com *args e retorne os valores ordenados de forma decrescente.

# def ordenados(*valores):
#     return sorted(valores, reverse=True)




# crie uma classe que represente um automovel com os atributos
# ano de fabricação
# marca
# preço
# métodos get_ano, get_marca e get_preco

class Automovel():
    '''Classe que representa um automovel'''
    def __init__(self, ano, marca, preco):
        self.ano = ano
        self.marca = marca
        self.preco = preco

    def get_ano(self):
        print(self.ano)

    def get_marca(self):
        print(self.marca)

    def get_preco(self):
        print(self.preco)

# crie uma classe Moto que terá
# o atributo tipo e herdará os atributos da classe automovel
# e os métodos: ligar, desligar, acelerar, frear
# obs.: lembre-se que a moto só pode ligar se estiver desligada e desligar quando ligada
# acelerar e frear também só ligada




ligada = False
class Moto(Automovel):
    '''Classe que representa uma Moto'''
    def __init__(self, ano, marca, preco, tipo='Moto'):
        super().__init__(ano, marca, preco)
        self.tipo = tipo

    def Ligar(self):
        self.ligada = False
        try:
            if self.ligada == False:
                print('Ligando...')
                print('Ligada...')
                ligada = True
            else:
                raise TypeError('Ligue a moto')
        except TypeError as motoDesligada:
            print('motoDesligada')

    def desligar(self):
        self.ligada = True
        try:
            if self.ligada == True:
                print('Desligando...')
                print('Desligada...')
                ligada = False
            else:
                raise TypeError('Desligue a moto')
        except TypeError as motoLigada:
            print('motoLigada')
            
    def acelerar(self):
        try:
            if self.ligada == False:
                print('Acelerou...')

    def Frear(self):
        try:
            if self.ligada == True:
                print('Freou...')
