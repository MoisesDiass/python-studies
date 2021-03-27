larg = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
area = larg*alt
latasdetintas = area/2
print('voce precisara de {} latas de um litro de tinta pra pintar a sua parede com {}M de area'.format(
    latasdetintas, area))
