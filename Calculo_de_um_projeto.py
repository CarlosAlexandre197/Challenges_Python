'''Um freelancer está com dificuldade para calcular qual valor cobrar por um projeto que está estimado em 80 horas. 
Após pensar e revisitar o preço de alguns projetos que cobrou no passado, ele montou a seguinte fórmula: 
valor inicial + quantidade de horas estimadas * valor da hora + 15% do valor calculado.

Crie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre será R$ 1000,00 e o valor da hora 
cobrada é de R$ 20,45. A aplicação deve imprimir o valor calculado pelo projeto considerando duas casas decimais na formatação do valor.'''

horas_estimadas = 80
valor_inicial = 1000.00
valor_hora = 20.45
taxa = 0.15 

valor_total = (valor_inicial + horas_estimadas * valor_hora) * (1 + taxa)

print(f'{valor_total:.2f}')