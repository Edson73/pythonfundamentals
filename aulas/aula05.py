# manipulando arquivos

# arq1 = '../arquivos/sherlock.txt'

# with open(arq1, 'r+') as f:
#     print(f.readlines())

# print(arq1.read()) # mostra conteúdo do arquivo
# print(arq1.tell()) # conta quantos caracteres LEU
# arq1.seek(3,2)
# print(arq1.read(500))
# arq1.close()

# with open('arquivo01.txt', 'x') as f:
#     f.write('Abrindo arquivos em python')

# try:
#     data = request_api_data()
# except RuntimeError as error:
#     retry('5 minutes')
# else:
#     try:
#         insert_in_database()
#     except RuntimeError as erro2:
#         print(erro2)

# def soma(x, y):
#     return x + y

# print(soma(10, 13))

# produtos = []

# def cadastraProduto(produto):
#     produtos.append(produto)

# def listarProdutos():
#     for p in produtos:
#         print(p)

# produto = ""

# while produto != "sair":
#     produto = input('Digite o produto que deseja cadastrar: ')
#     cadastraProduto(produto)
#     print('Produtos cadastrados')
#     listarProdutos()

# def soma(x, y):
#     return x + y

# def primo(num):
#     for n in range(2, num):
#         if num % n == 0:
#             print('Não é primo')
#             break
#         else:
#             print('É primo')

# primo(3)

# def alternaServidor(atual, novo):
#     print('O IP atual é:', atual)
#     print('O novo IP é:', novo)

# alternaServidor('192.168.1.1', '192.168.1.254')

# def conexao():
#     r = requests.get('https://google.com')

#     print(r.status_code)

# conexao()

# def media(x, y):
#     return(x + y) / 2

# print(media(10,2))


# ARGS E KWARGS

# def printa(*valores):
#     print(valores)
# printa('nome', 'sobrenome', 'outro')

# def printa2(**valores):
#     print(valores)
# printa2(key1='valor', key2='valor2', key3='valor3')

# criar uma função que muda o valor de nome e print na tela
# nome = 'Joao'
# def mudaNome(novo_nome):
#     nome = novo_nome
#     return nome
# print(mudaNome('Ana'))

# texto = 'Eu sou um cérebro, Watson. O resto é mero apêndice.'
# def split_texto(text):
#     return text.split(' ')
# def lower_texto(text):
#     return text.lower()
# arquivo_split = split_texto(texto)
# arquivo_lower = lower_texto(texto)

