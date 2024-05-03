'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários e Ordenação
Objetivo: Solução do problema beecrowd 1515 - Hello Galaxy
          https://www.beecrowd.com.br/judge/pt/problems/view/1515

Linha de comando para executar: python3 beecrowd_1515.py'''

n = int(input())

while n!=0:
    
    dic = {}
    
    for _ in range(n):
        planeta_origem,ano,duracao=input().split()
        ano = int(ano)
        duracao = int(duracao)
        dic[ano-duracao] = planeta_origem
    
    saidas_ord = sorted(dic)
    
    print(dic[saidas_ord[0]])
    
    n = int(input())
