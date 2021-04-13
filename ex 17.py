import math
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
co2 = co*co
ca2 = ca*ca
hip2 = co2+ca2
hip = math.sqrt(hip2)
print('O valor da Hipotenusa é {:.2f}'.format(hip))
