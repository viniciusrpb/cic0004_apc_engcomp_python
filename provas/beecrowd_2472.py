'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2472 - Tapetes
   Prof. Dr. Vinicius Ruela Pereira Borges '''

l,n = map(int,input().split())

'''Estrategia para maximizar a soma dos tapetes:
como a area de um tapete eh dada por um produto do tipo
a x a, quanto maior o valor de a, maior eh seu produto

Entao se temos que transportar obrigatoriamente
n tapetes, pegamos n-1 tapetes para ter area 1x1
e o tapete restante para ter comprimento p = l-(n-1)

logo sua area eh p x p

a resposta entao fica

area = (n-1) + p x p
'''

maior = l-(n-1)

area = maior*maior + n-1

print(area)

