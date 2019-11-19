# -*- coding: utf-8 -*-
# Dicionarios
# endereco = {'logradouro': 'Rua Vergueiro',
#             'numero': '3057',
#             'bairro': 'Vila Mariana',
#             'cidade': 'São Paulo',
#             'UF': 'SP',
#             'CEP': '04101-300'
# }
# endereco_2 = {'logradouro': {'user1': 'Rua vergueiro',
#                               'user2': 'Rua Augusta'
# },
#             'numero': {'user1': '3057',
#                         'user2': '1050'
#                         },
#             'bairro': {'user1':'vila mariana',
#                         'user2': 'cerqueira cesar'
#                         },
#             'cidade': {'user1':'sao paulo',
#                         'user2': 'sao paulo'},
#             'UF': {'user1':'SP',
#                     'user2':'SP'
#                     },
#             'cep': {'user1':'04101-300',
#                     'user2': '01212-030'}            
# }
# print(endereco.keys()) #retorna as chaves
# print(endereco.values()) # retorna os valores
# print(endereco.items())
# endereco_2.__setitem__('numero', {'user1': '3057', 'user2': '1030'
#                         })
# endereco_2['logradouro']['user2'] = '1030'
# print(endereco_2)

# var_dict = dict(nome='Edson', sobrenome='Osawa') # convertendo para um dicionario
# var_str = '5' # conversão de valores
# var_int = int(var_str) # conversão de valores
# var_float = float(var_int) # conversão de valores
# print(var_str, var_int, var_float)

# concatenar e inserir dados - duas maneiras de usar
# municipios_br = '5.570'
# estados_br = '26'
# brasil = 'O Brasil é uma república federativa formada pela união de {} estados federados, {} municípios e do Distrito Federal.'.format(estados_br, municipios_br)
# print(brasil)
# brasil2 = f'O Brasil é uma república federativa formada pela união de {estados_br} estados federados, {municipios_br} municípios e do Distrito Federal.'
# print(brasil2)

# teste = 'teste'
# teste2 = 'teste2'
# print(teste+teste2) # concatenação é com '+'

# num = 4
# print(hex(num))

# t = 1, 2
# l = list(t)
# print(l)