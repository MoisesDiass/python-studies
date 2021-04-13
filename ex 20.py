import random
nome1 = input('nome do aluno: ')
nome2 = input('nome do aluno: ')
nome3 = input('nome do aluno: ')
nome4 = input('nome do aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('a ordem da apresentaçao do trabalho é: {}'.format(lista))
