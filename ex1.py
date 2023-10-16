def nota_prova(n1, n2):
    resultado = (n1 + n2) / 2
    if resultado > 6:
        print('Aprovado!')
    else:
        print('Reprovado!')

nota1 = int(input('Insira a nota da sua primeira prova'))
nota2 = int(input('Insira a nota da sua segunda prova'))

nota_prova(nota1, nota2)
