'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Estruturas Condicionais (Python)
Objetivo: Solução do problema beecrowd 2375 - Sedex (OBI - Olimpíada Brasileira de Informática 2010)
          https://www.beecrowd.com.br/judge/pt/problems/view/2375

Linha de comando para executar: python3 beecrowd_2375_or.py
'''

diametro = int(input())

altura,largura,profundidade = input().split()
altura = int(altura)
largura = int(largura)
profundidade = int(profundidade)

if diametro > altura or diametro > largura or diametro > profundidade:
    print('N')
else:
    print('S')
