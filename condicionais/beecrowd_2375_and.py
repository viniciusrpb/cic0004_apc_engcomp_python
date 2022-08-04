'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Estruturas Condicionais (Python)
Objetivo: Solução do problema beecrowd 2375 - Sedex (OBI - Olimpíada Brasileira de Informática 2010)
          https://www.beecrowd.com.br/judge/pt/problems/view/2375

Linha de comando para executar: python3 beecrowd_2375_and.py
'''

diametro = int(input())

altura,largura,profundidade = (int(x) for x in input().split())

if diametro <= altura and diametro <= largura and diametro <= profundidade:
    print('S')
else:
    print('N')
