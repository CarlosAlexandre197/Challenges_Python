'''001 - Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar.'''

def par_impar(numero):
  if numero % 2 == 0:
    return "Par"
  else:
    return "Impar"

print(par_impar(2))

'''002 - Crie uma função que recebe um número inteiro por parâmetro e então imprime na tela do número recebido até o zero.'''

def mostra_ate_zero(numero):
  while numero >= 0:
    print(numero)
    numero -= 1

mostra_ate_zero(2)

'''003 - Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma.'''

def soma_3_numeros(a, b, c):
  return a + b + c

print(soma_3_numeros(3, 6, 2))

'''004 - Crie um programa que seja capaz de obter e somar todos os números passados pelo usuário como entrada, 
permitindo somar qualquer quantidade de dados de entrada.'''

soma = 0
numero = int(input())
while (numero != -1):
  soma += numero
  numero = int(input())
print(soma)

'''005 - Faça um programa com uma função que necessite de um parâmetro. A função deve retornar "Positivo",
se seu o número for maior que zero, "Negativo" se o número for menor que zero, e "Zero" se o número for igual a zero.'''

def positivo_negativo_zero(numero):
  if numero == 0:
    return "Zero"
  elif numero > 0:
    return "Positivo"
  else:
    return "Negativo"

print(positivo_negativo_zero(5))

'''006 - Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, 
calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.'''

def gorjeta(valor, porcentagem):
  return valor * porcentagem / 100

resultado = gorjeta(100, 15)
print(f"{resultado:.2f}")

'''007 - Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma palavra. 
A letra desejada e a palavra a ser verificada serão passadas por parâmetro para a função, 
que retornará a quantidade da letra na palavra.'''

def conta_letras(letra_buscada, palavra):
  contagem = 0 
  for letra_atual in palavra:
    if letra_atual == letra_buscada:
      contagem += 1
  return contagem

saida = conta_letras('a', 'abelha')
print(saida)

'''008 - Crie uma função que receba duas palavras e retorne "True" caso a primeira palavra seja um prefixo da segunda, 
e "False" caso contrário.'''

def verifica_prefixo(palavra1, palavra2):
  tamanho = len(palavra1)
  for indice in range(tamanho):
    if palavra1[indice] != palavra2[indice]:
      return False
  return True

resultado = verifica_prefixo('programa', 'programador')
print(resultado)
