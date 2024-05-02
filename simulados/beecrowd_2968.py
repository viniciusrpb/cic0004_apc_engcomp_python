'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2968 - Hora da Corrida
   Prof. Dr. Vinicius Ruela Pereira Borges '''

import math

v,n = map(int,input().split())

total_placas = v*n

ans_linha = ''
for p in range(10,100,10):
    ans = math.ceil((p*total_placas)/100)
    ans_linha+=str(ans)+' '

print(ans_linha[:-1])
