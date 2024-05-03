'''Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Strings ou Matemática Básica
Objetivo: Solução do problema beecrowd 2867 - Digitos
          https://www.beecrowd.com.br/judge/pt/problems/view/2867

Linha de comando para executar: python3 beecrowd_2867.py'''

c = int(input())

for _ in range(0,c):
    n,m = map(int,input().split())
    p = n**m
    ans = len(str(p))
    print(ans)
