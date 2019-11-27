# def oi(nome='Pedro'):
#     return "Oi " + nome


#     def ola():
#         return 'Aqui você está na função ola()'

#     def boasvindas():
#         return 'aqui você está na função voasvindas()'



def inc(x):
    return x + 1

def dec(x):
    return x - 1

def soma_2(y):
    return y + 2

def printa(x):
    print(x)

def operacao(func, x):
    resultado = func(x)
    return resultado


print(operacao(printa, 10))
