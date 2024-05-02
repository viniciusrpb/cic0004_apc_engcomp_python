'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Matrizes
Objetivo: Solução do problema beecrowd 2471 - Matrizes
          https://www.beecrowd.com.br/judge/pt/problems/view/2471

Linha de comando para executar: python3 beecrowd_2471.py'''

n = int(input())

matriz = []
for _ in range(n):
	matriz.append([int(x) for x in input().split()])
	
linhas = []
for i in range(n):
	s=0
	for j in range(n):
		s+=matriz[i][j]
	linhas.append(s)

colunas = []
for j in range(n):
	s=0
	for i in range(n):
		s+=matriz[i][j]
	colunas.append(s)
	
dic = {}
for i in range(0,len(linhas)):
	if linhas[i] in dic:
		dic[linhas[i]]+=1
	else:
		dic[linhas[i]] = 1

mudou=-1
for chave in dic:
	if dic[chave] == 1:
		mudou = chave

ans_i = -1
for i in range(0,len(linhas)):
	if linhas[i] == mudou:
		ans_i=i
 
 
dic = {}
for j in range(0,len(colunas)):
	if colunas[j] in dic:
		dic[colunas[j]]+=1
	else:
		dic[colunas[j]] = 1

mudou=-1
soma_certa=-1
for chave in dic:
	if dic[chave] == 1:
		mudou = chave
	else:
		soma_certa=chave

ans_j = -1
for j in range(0,len(colunas)):
	if colunas[j] == mudou:
		ans_j=j
		
num = mudou - matriz[ans_i][ans_j]

orig = soma_certa-num

print(f'{orig} {matriz[ans_i][ans_j]}')
