'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 2312 - Quadro de Medalhas
          https://www.beecrowd.com.br/judge/pt/problems/view/2312
          
Linha de comando para executar: python3 beecrowd_2312.py'''

def comp(pais1,pais2,i):
    if i == 3:
        if pais1[i] > pais2[i]:
            return True
        else:
            return False
        
    if pais1[i] == pais2[i]:
        return comp(pais1,pais2,i+1)
    else:
        if pais1[i] < pais2[i]:
            return True
        else:
            return False
            
n = int(input())

paises = []
for _ in range(0,n):
    nome,o,p,b = input().split()
    paises.append([int(o),int(p),int(b),nome])
    
for i in range(0,n-1):
        for j in range(i+1,n):
            if comp(paises[i],paises[j],0) == True:
                aux = paises[i]
                paises[i] = paises[j]
                paises[j] = aux
    

for i in range(n):
    print(f'{paises[i][3]} {paises[i][0]} {paises[i][1]} {paises[i][2]}')
