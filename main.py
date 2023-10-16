def exibir_mensagem():
    print(f'olá, tudo bem')

def par_impar(numero):
    if numero % 2 == 0:
        print('numero par \n')
    else:
        print('impar')

def area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'a area do triangulo é {area} \n')

def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

exibir_mensagem()

n = int(input('numero: '))
par_impar(n)

base = int(input('insira a base de um triangulo \n'))
altura = int(input('insira a altura de um triangulo \n'))
area_triangulo(base, altura)

base_retangulo = int(input('insira a base de um retangulo \n'))
altura_retangulo = int(input('insira a altura de um retangulo \n'))
c = calcular_area_retangulo(base_retangulo, altura_retangulo)
print(f'a area de um retangulo é {c} \n')
