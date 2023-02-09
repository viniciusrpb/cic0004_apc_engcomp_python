'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 1261 - Pontos de Feno
          https://www.beecrowd.com.br/judge/pt/problems/view/1261
          
Linha de comando para executar: python3 beecrowd_1261.py
'''

while True:

    try:

        empl = {}

        m,n = (int(x) for x in input().split())

        for _ in range(0,m):
            e,s = input().split()
            s = int(s)
            empl[e]=s

        for _ in range(0,n):
            text = input()
            ans = 0
            while text != '.':
                for word in text.split():
                    if word in empl:
                        ans+=empl[word]
                text = input()

            print(ans)

    except EOFError:
        break
