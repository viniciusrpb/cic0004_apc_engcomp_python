'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Recursividade (Python)
Objetivo: Solução do problema beecrowd 1441 - Hailstone Sequences
          https://www.beecrowd.com.br/judge/pt/problems/view/1441
Linha de comando para executar: python3 beecrowd_1441.py
'''

def hailstone(hn_1):

    if hn_1 == 1:
        return 1

    if hn_1 % 2 == 0:
        hn = hailstone(hn_1//2)
    else:
        hn = hailstone(3*hn_1 + 1)

    return max(hn_1,hn)

n = int(input())

while n>0:
    ans = hailstone(n)
    print(f'{ans}')
    n = int(input())
