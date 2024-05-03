'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 2633 - Churras no Yuri
          https://www.beecrowd.com.br/judge/pt/problems/view/2633
          
Linha de comando para executar: python3 beecrowd_2633.py
'''

while True:
    
    try:
        
        n = int(input())
        
        dic = {}
        
        for _ in range(0,n):
            carne,validade = input().split()
            validade = int(validade)
            dic[validade] = carne
        
        ans = ''
        for val in sorted(dic):
            ans+=dic[val]+" "
        print(ans[:-1])
        
    except EOFError:
        break
