dia = int(input('Quantos dias voce ficou com o carro? '))
precoDoDia = dia*60
km = float(input('Quantos Km voce andou com o carro?'))
precoPorKm = km * 0.15
precoFinal = precoDoDia + precoPorKm
acrescimoTaxa = precoFinal * 5 / 100
precoFinalComTaxa = precoFinal + acrescimoTaxa
print('O total a pagar é: R${} Mas com o acrescimo de 5% o preço final fica em: R${}'.format(
    precoFinal, precoFinalComTaxa))
