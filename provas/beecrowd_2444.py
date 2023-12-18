'''Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Listas
Objetivo: Solução do problema beecrowd 2444 - Volume da TV
          https://www.beecrowd.com.br/judge/pt/problems/view/2444

Linha de comando para executar: python3 beecrowd_2444.py'''

v,t = map(int,input().split())

volumes = [int(x) for x in input().split()]

for i in range(0,t):
    v+=volumes[i]
    if v > 100:
        v = 100
    elif v < 0:
        v = 0

print(v)
