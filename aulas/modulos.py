# import aula07, pwd
import os, sys

# os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]

# print(os.getlogin())

# print(os.listdir('/home/developer'))

# print(os.rename('./base.py', 'pandas.py'))

# os.system('echo $USER')

# print(sys.platform)

# print(sys.builtin_module_names)

# print(sys.argv)

# sys.exit()

# lista = [1,2,3,4,5,23,6,7,8]
# print(len(lista))

# for i in range(len(sys.argv)):
#     if i ==0:
#         print(f'Function name: {sys.argv[0]}')
#     else:
#         print(f'{i}. argument: {sys.argv[1]}')


# import datetime

# print(datetime.datetime.now())
# print(datetime.timedelta(7))
# print(datetime.time(14,0,0))
# print(datetime.date(2017,1,1))


# from datetime import datetime

# acesso = datetime(2019, 10, 12, 00,00,00)
# atual = datetime.now()

# if(atual - acesso).total.seconds() > 3600:
#     print('Seu token expirou')
# else:
#     print('Acesso liberado')



# import csv



# with open('../arquivos/salarios.csv', 'w', newline='') as csvfile:
#     arquivo = csv.writer(csvfile, delimiter=',')
#     arquivo.writerow(['Teste'] * 5)
#     arquivo.writerow(['4linux', 'Python'])