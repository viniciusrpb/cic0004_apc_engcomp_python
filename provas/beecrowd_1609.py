'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 1609 - Contando Carneirinhos
          https://www.beecrowd.com.br/judge/pt/problems/view/1609

Linha de comando para executar: python3 beecrowd_1609.py'''

t = int(input())

while t > 0:

    n = int(input())

    sonho = [int(x) for x in input().split()]

    dic = {}

    for carneiro in sonho:
        if carneiro not in dic:
            dic[carneiro]=1

    print(len(dic))

    t-=1
