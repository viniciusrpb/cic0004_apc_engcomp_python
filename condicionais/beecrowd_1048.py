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

def solve(salario_atual,perc):
    
    novo_salario = salario_atual + salario_atual*(perc/100)
    reajuste = novo_salario - salario_atual
    
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {perc} %')
    
salario = float(input())

if salario > 2000.00:
    solve(salario,4)
elif salario > 1200.00:
    solve(salario,7)
elif salario > 800.00:
    solve(salario,10)
elif salario > 400.00:
    solve(salario,12)
else:
    solve(salario,15)
