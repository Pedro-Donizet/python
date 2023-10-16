def poligono(numero_lados):
    if numero_lados == 3:
        print('Poligono!')
    if numero_lados == 4:
        print('Quadrilatero!')
    if numero_lados == 5:
        print('Pentagono!')
    if numero_lados != 3 or numero_lados != 4 or numero_lados != 5:
        print('Numero de lado invalidos')

numero = int(input('Insira o numero de lados de um poligono'))
poligono(numero)
