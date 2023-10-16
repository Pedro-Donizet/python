def ler_numero():
    numero = int(input('insira um numero inteiro: '))

    return numero
def tabuada(n):
    for i in range(11):
        calculo = n * i
        print(f'{n} X {i} = {calculo}')

inteiro = ler_numero()

tabuada(inteiro)

