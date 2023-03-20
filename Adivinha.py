'''Faça um programa que o usuário precise tentar advinhar um número de 1 a 10.'''

from random import randint

numero = randint(1, 10)

chute = int(input('Digite um número: '))

print(numero == chute)

print(numero)


#Exemplo: 02

from random import randint

numero = randint(1, 10)

chute = int(input('Digite um número: '))

if chute == numero:
    print('Parabéns você acertou!')
if chute == numero:
    print('FIM DO PROGRAMA!')

else:
    print('Você errou...Tente novamente!')
