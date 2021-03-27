saldo = int(input('Digite seu saldo: '))
dolarHoje = float(input('Digite o valor do dólar hoje: '))

saldoEmDolar = saldo/dolarHoje

print('voce possui U$ {:.2f} em conversao direta com seus R$ {:.2f}'.format(
    saldoEmDolar, saldo))
