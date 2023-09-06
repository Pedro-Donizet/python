nome = input('digite o nome do vendedor: ')
quantidade = int(input('quantos carros foram vendidos: '))
valor = float(input('digite o valor total das vendas: '))

comissao = 200* quantidade
acressimo = valor * 2 / 100

total = 2500 + 200 * quantidade + valor * 2 / 100

print(f'valor final: {total}')