'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Exercício de Prática (Python)
Objetivo: Solução do problema beecrowd 2786 - School Floor
          https://www.beecrowd.com.br/judge/en/problems/view/2786

Linha de comando para executar: python3 beecrowd_2786.py
'''

L = int(input())
C = int(input())

type1 = L*C + (L-1)*(C-1)
type2 = 2*(L-1) + 2*(C-1)

print(type1)
print(type2)
