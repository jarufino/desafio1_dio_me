menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [x] Sair
=> '''

saldo = 0
limite = 100
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do depósito: R$ '))
        if valor > 0:
            if limite < 100:
                limite_a_ser_adicionado = min(100 - limite, valor)
                limite += limite_a_ser_adicionado
                valor -= limite_a_ser_adicionado
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! Valor informado é inválido.')

    elif opcao == 's':
        valor = float(input('Informe o valor para saque: R$ '))
        total_disponivel = saldo + limite
        excedeu_total_disponivel = valor > total_disponivel
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_total_disponivel:
            print('Operação falhada! Saldo e limite insuficientes.')
        elif excedeu_saques:
            print('Falha, número máximo de saques ultrapassado.')
        elif valor > 0:
            if valor <= saldo:
                saldo -= valor
            else:
                restante = valor - saldo
                saldo = 0
                limite -= restante
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print('Sr(a) cliente, o valor informado é inválido.')

    elif opcao == 'e':
        print('\n============================EXTRATO============================')
        print('Sem realização de movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}\nLimite: R$ {limite:.2f}')
        print('=================================================================')

    elif opcao == 'x':
        break
    else:
        print('Operação inválida, por favor entre com a opção desejada.')
