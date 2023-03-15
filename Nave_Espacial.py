'''Uma nave espacial recebe as pessoas com uma mensagem de boas vindas de acordo com o nome que elas forneceram ao fazer o cadastro 
na recepção. Crie um programa que imprima a mensagem de boas vindas de acordo com os nomes na lista: 
nomes = [Elysson, Giulia, Willian, Gileno], com a seguinte mensagem: 
“Olá, NOME_PESSOA! Seja bem vindo à nave Imperial dos Siths.”. 
Nessa aplicação faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo nome lido na lista 
e imprimindo a frase de boas vindas com o nome substituído.'''

nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno']


for nome in nomes:
    print(f'Olá, {nome}! Seja bem vindo à nave Imperial dos Siths.')

