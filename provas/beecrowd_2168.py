'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Matriz
Objetivo: Solução do problema beecrowd 2168 - Crepusculo em Portland
          https://beecrowd.com.br/judge/pt/problems/view/2168

Linha de comando para executar: python3 beecrowd_2168.py'''

n = int(input())

matriz = []

for i in range(0,n+1):
    matriz.append([int(x) for x in input().split()])

for i in range(0,n):
    string = ''
    for j in range(0,n):
        ans = matriz[i][j]+matriz[i][j+1]+matriz[i+1][j+1]+matriz[i+1][j]
        if ans >= 2:
            cel = 'S'
        else:
            cel = 'U'
        string+=cel
    print(string)
