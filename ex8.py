while True:
    def menu():
        escolha = int(input('calculadora\n'
                            '1- adição\n'
                            '2- subtração\n'
                            '3- multiplicação\n'
                            '4- divisão\n'
                            '5- sair do programa\n'
                            'Escolha sua opção:'))
        return escolha

    def adicao(n1, n2):
        conta = n1 + n2
        return conta

    def subtracao(n1, n2):
        conta = n1 - n2
        return conta

    def multiplicacao(n1, n2):
        conta = n1 * n2
        return conta

    def divisao(n1, n2):
        conta = n1 / n2
        return conta

    escolha = menu()
    if escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
        print('insira uma opçao valda')
        menu()

    if escolha == 1:
        numero1 = int(input('insira um numero: '))
        numero2 = int(input('insira mais um numero: '))
        adicao(numero1, numero2)
        print(f'{adicao(numero1, numero2)}')


    if escolha == 2:
        numero1 = int(input('insira um numero: '))
        numero2 = int(input('insira mais um numero: '))
        subtracao(numero1, numero2)
        print(f'{subtracao(numero1, numero2)}')
    if escolha == 3:
        numero1 = int(input('insira um numero: '))
        numero2 = int(input('insira mais um numero: '))
        multiplicacao(numero1, numero2)
        print(f'{multiplicacao(numero1, numero2)}')

    if escolha == 4:
        numero1 = int(input('insira um numero: '))
        numero2 = int(input('insira mais um numero: '))
        divisao(numero1, numero2)
        print(f'{divisao(numero1, numero2)}')

    if escolha == 5:
        exit()

