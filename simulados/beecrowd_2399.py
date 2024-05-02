'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Listas
Objetivo: Solução do problema beecrowd 2399 - Campo Minado
          https://www.beecrowd.com.br/judge/pt/problems/view/2399
          
Linha de comando para executar: python3 beecrowd_2399.py'''

n = int(input())

lista = [0]

for i in range(0,n):
	lista.append(int(input()))

lista.append(0)

for k in range(1,n+1):
	elem = lista[k-1]+lista[k]+lista[k+1]
	print(elem)
	
