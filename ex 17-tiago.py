import math
catetoOposto = float(input('Digite o cateto oposto: '))
catetoAdjacente = float(input('Digite o cateto adjacente: '))

# soma = cateto oposto² + cateto adjacente²
somaDosCatetos = (catetoOposto ** 2) + (catetoAdjacente ** 2)

hipotenusa = math.sqrt(somaDosCatetos)

print('A hipotenusa vale {:.2f} graus'.format(hipotenusa))
