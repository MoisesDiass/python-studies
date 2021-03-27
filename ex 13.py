salario = float(input('digite seu salario: R$ '))
aumento = salario*15/100
salarioFinal = salario+aumento
print('Parabens o seu salario acabou de aumentar de R$ {} para R${}'.format(
    salario, salarioFinal))
