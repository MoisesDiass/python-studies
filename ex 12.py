preco = int(input('digite o preço do produto: '))
desc = preco*5/100
precoFinal = preco - desc
print('O preço final do seu produto é: R$ {}'.format(precoFinal))
