'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 1709 - Baralho Embaralhado
          https://www.beecrowd.com.br/judge/pt/problems/view/1709
          
Linha de comando para executar: python3 beecrowd_1709.py
'''

p = int(input())
n = p//2

ans = 0

carta = 1

flag_esq = True

while carta != n or flag_esq == True:
    
    if flag_esq == True:
        carta=carta*2
    
        if carta > n:
            carta=p-carta+1
            flag_esq = False
    else:
        carta=carta*2
        
        if carta > n:
            carta=p-carta+1
            flag_esq = True
        
    ans+=1


print(ans+1)
