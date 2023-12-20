'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários e Listas
Objetivo: Solução do problema beecrowd 2469 - Notas
          https://www.beecrowd.com.br/judge/pt/problems/view/2469

Linha de comando para executar: python3 beecrowd_2469.py'''

n = int(input())

freq_notas = {}

lista = [int(x) for x in input().split()]

for x in lista:
	if x in freq_notas:
		freq_notas[x]+=1
	else:
		freq_notas[x]=1


maior = 0
ans = -1
for nota in freq_notas:
	if freq_notas[nota] > maior:
		maior = freq_notas[nota]
		ans = nota
	elif freq_notas[nota] == maior and nota > ans:
		ans = nota

print(ans)
