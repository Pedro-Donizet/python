def pesoIdeal(altura, sexo):
    if sexo == 'M' or sexo == 'masculino':
        calculo = (72.7 * altura) - 58
    if sexo == 'F' or sexo == 'feminino':
        calculo = (62.1 * altura) - 44.7
    return calculo

sexo = input('Insira seu sexo: ')
altura = float(input('insira sua altura'))

calculo = pesoIdeal(altura, sexo)
print(f'{calculo}')
