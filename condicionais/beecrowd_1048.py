'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Estruturas Condicionais (Python)
Objetivo: Solução do problema beecrowd 1048 - Aumento de Salário
          https://www.beecrowd.com.br/judge/pt/problems/view/1048
Linha de comando para executar: python3 beecrowd_1048.py
'''

salario = float(input())

if salario > 2000.00:
    reajuste = 4
elif salario > 1200.00:
    reajuste = 7
elif salario > 800.00:
    reajuste = 10
elif salario > 400.00:
    reajuste = 12
else:
    reajuste = 15

reajuste2 = reajuste/100
reajuste_ganho = reajuste2*salario
novo_salario = salario + reajuste_ganho

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {reajuste} %')


