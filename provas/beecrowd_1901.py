'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários e Matrizes
Objetivo: Solução do problema beecrowd 1901 - Borboletas
          https://www.beecrowd.com.br/judge/pt/problems/view/1901

Linha de comando para executar: python3 beecrowd_1901.py'''

n = int(input())

borboletas = []

especies = {}

for _ in range(0,n):
    linha = [int(x) for x in input().split()]
    borboletas.append(linha)

for _ in range(0,2*n):
    x,y = map(int,input().split())
    especie_borboleta = borboletas[x-1][y-1]
    if especie_borboleta not in especies:
        especies[especie_borboleta] = 1

print(len(especies))
