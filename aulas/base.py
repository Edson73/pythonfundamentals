import pandas as pd

df = pd.read_csv('../arquivos/salarios.csv')

print(df['Name'])

var = df['nome e salario'] = df['Name'] + ' ' + df['Employee Annual Salary']

df.to_csv('name_salario.csv', header=0)

# var.to_csv('name.csv', header=0)

# parametros loc: numero da linha
# print(df.loc[20, ['Name', 'Employee Annual Salary']])
var2 = df.loc[20, ['Name', 'Employee Annual Salary']]

# parametors do iloc: numero da linha, index da coluna

print(df.iloc[10, 3])

# df.to_csv('novo_salario.csv', header=0, sep=';')
# print(dt.iloc[50:]) # do 50 até o fim # iloc pega pelo número da linha (index)

# print(dt.loc[:50]) # do inicio até o 50 loc pega pelo número de linhas