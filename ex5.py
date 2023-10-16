def area(raio):
    calculo = 3.14 * raio ** 2
    return calculo
def perimetro(raio):
    calculo = 3.14 * 2 * raio
    return calculo

raio = int(input('insira a area de um circulo'))

area = area(raio)

perimetro = perimetro(raio)

print(f'{area}')
print(f'{perimetro}')
