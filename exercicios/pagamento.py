# -*- coding: utf-8 -*-

print('Software de folha de pagamento!')

vr_hora = float(input('Digite o valor da hora:'))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = vr_hora * qtd_hora

if salario_bruto >= 4600:
    aliquotaIR = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    aliquotaIR = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    aliquotaIR = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    aliquotaIR = 7
else:
    aliquotaIR = 0

valorIR = salario_bruto * (aliquotaIR / 100.0)

valor_sindicato = salario_bruto * (3 / 100.0)

total_descontos = valorIR + valor_sindicato

valorFGTS = salario_bruto * (11 / 100.0)

salario_liquido = salario_bruto - total_descontos

print(f'\nSalario Bruto: ({vr_hora} * {qtd_hora}): R$ {salario_bruto}')
print(f'(-) IR ({aliquotaIR}%): R${valorIR}')
print(f'(-) Sindicato (3%): R$ {valor_sindicato}')
print(f'FGTS (11%): R$ {valorFGTS}')
print(f'Total de Descontos: R$ {total_descontos}')
print(f'Salario Liquido: R$ {salario_liquido}')
