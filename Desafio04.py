'''Faça um programa que leia dois números inteiros, calcule e mostre na tela.
1. O produto do dobro do primeiro pela metade do segundo.
2. A soma do triplo do primeiro com o segundo.
3. O segundo elevado ao cubo.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

calculo1 = (n1 * 2) * (n2 / 2)
calculo2 = n1 * 3 + n2
calculo3 = n2 ** 3

print(f'Resultado 1: {calculo1:.0f}')
print(f'Resultado 2: {calculo2}')
print(f'Resultado 3: {calculo3}')
