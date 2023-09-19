'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Variaveis, Expressoes e Instrucoes
Objetivo: Solução do problema beecrowd 3346 - Flutuação do PIB
          https://www.beecrowd.com.br/judge/pt/problems/view/3346
Linha de comando para executar: python3 beecrowd_3346.py

Seja o pib_atual o PIB de um determinado ano e ans a variável de resposta:

pib_1ano = f1*pib_atual + pib_atual
pib_2anos = f2*pib_1ano + pib_1ano

pib_2anos = ans*pib_atual + pib_atual
pib_2anos - pib_atual = ans*pib_atual
f2*pib_1ano + pib_1ano - pib_atual = ans*pib_atual
f2*(f1*pib_atual + pib_atual) + f1*pib_atual + pib_atual - pib_atual = ans*pib_atual
f2*(f1*pib_atual + pib_atual) + f1*pib_atual = ans*pib_atual
f2*f1*pib_atual + f2*pib_atual + f1*pib_atual = ans*pib_atual

Cortando os pib_atual, temos:

ans = f1 + f2 + f1*f2
'''

f1,f2 = map(float,input().split())

f1/=100
f2/=100

ans = f2*f1 + f2 + f1
ans=ans*100

print(f'{ans:.6f}')


    

