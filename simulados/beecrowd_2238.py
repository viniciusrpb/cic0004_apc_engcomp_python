'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2238 - Divisores
   Prof. Dr. Vinicius Ruela Pereira Borges '''

import math

a,b,c,d = map(int,input().split())

''' se os dados de entrada nao satisfazerem
a descricao do enunciado, nao ha como obter resposta'''
if c % a != 0 or a%b == 0 or c < a:
    ans = -1
else:
    n = a
    achou = False

    while achou == False and n <= math.ceil(1000000000): #sempre vamos encontrar uma resposta

        if c % n == 0:

            if n % a == 0 and n % b != 0 and d % n != 0:
                ans = n
                achou = True
        n+=a # caminha pelos multiplos de a (reduz a quantidade total de operacoes)

print(ans)
