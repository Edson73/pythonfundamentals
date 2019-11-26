# -*- coding : utf-8 -*-

'''
Software do OldBank:
                    Atributos:
                            Número do Banco;
                            Número da Agência;
                            Númro da conta;
                            Nome do cliente;
                            Saldo;
                            
                    Métodos:
                            Sacar;
                            Depositar;
                            Extrato;
'''

class ContaBancaria():

    def __init__(self, cliente, conta, ag=8, banco=999, saldo=0):
        self.cliente = cliente
        self.conta = conta
        self.agencia = ag
        self.banco = banco
        self.saldo = saldo
    
    def depositar(self):
        deposito = float(input('Digite o valor a ser depositado: R$'))
        print(f'Saldo Anterior R${self.saldo}')
        print(f'Deposito: R${deposito}')
        self.saldo += deposito
        print(f'Novo Saldo: R${self.saldo}')

    def sacar(self):
        saque = float(input('Digite o valor a ser sacado: R$'))
        if self.saldo < saque:
            print('Saldo insuficiente')
        
        else:
            print(f'Saldo Anterior: R${self.saldo}')
            print(f'Saque: R${saque}')
            self.saldo -= saque
            print(f'Novo Saldo: R${self.saldo}')
    
    def extrato(self):
        print('Extrato')
        print('=' * 20)
        print(f'Agência: 0{self.agencia} Conta: {self.conta}')
        print(f'Cliente: {self.cliente}')
        print(f'Saldo: R${self.saldo}')

cliente = ContaBancaria(input('Digite o nome do cliente: '), input('Digite o número da conta: '))
print('Bem vindo(a) ao OldBak!')
print('Selecione a opção abaixo:')
print('Digite 1 para Extrato')
print('Digite 2 para Deposito')
print('Digite 3 para Saque')



opcao = int(input('> '))

try:
    if opcao == 1:
        cliente.extrato()
    elif opcao == 2:
        cliente.depositar()
    elif opcao == 3:
        cliente.sacar()
    else:
        print('Opção inválida!')

except TypeError as e:
    print(e, 'Digite um valor válido')