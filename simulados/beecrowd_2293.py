'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2293 - Campo de Minhocas
   Prof. Dr. Vinicius Ruela Pereira Borges '''

n,m = map(int,input().split())

campo = []
for _ in range(0,n):
	linha = [int(x) for x in input().split()]
	campo.append(linha)

maior_linhas = -1
for i in range(0,n):
	s = 0
	3
	for j in range(0,m):
		s+=campo[i][j]
	if s > maior_linhas:
		maior_linhas = s
		
maior_colunas = -1
for j in range(0,m):
	s = 0
	for i in range(0,n):
		s+=campo[i][j]
	if s > maior_colunas:
		maior_colunas = s
		
print(f'{max(maior_colunas,maior_linhas)}')
