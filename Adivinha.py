'''Faça um programa que o usuário precise tentar advinhar um número de 1 a 10.'''

from random import randint

numero = randint(1, 10)

chute = int(input('Digite um número: '))

print(numero == chute)

print(numero)
