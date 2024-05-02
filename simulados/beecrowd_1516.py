'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Matrizes
Objetivo: Solução do problema beecrowd 1516 - Imagem
          https://www.beecrowd.com.br/judge/pt/problems/view/1516
          
Linha de comando para executar: python3 beecrowd_1516.py
'''

n,m = (int(x) for x in input().split())

while n!=0 and m != 0:

    matriz = [list(input()) for _ in range(0,n)]

    a,b = (int(x) for x in input().split())

    pa = a//n
    pb = b//m

    ans = [list(' '*b) for _ in range(0,a)]

    for i in range(0,n):

        for j in range(0,m):

            for aa in range(i*pa,i*pa+pa):
                for bb in range(j*pb,j*pb+pb):
                    ans[aa][bb] = matriz[i][j]


    for i in range(0,a):
        string = ''
        for j in range(0,b):
            string+=ans[i][j]
        print(string)
    print()

    n,m = (int(x) for x in input().split())
