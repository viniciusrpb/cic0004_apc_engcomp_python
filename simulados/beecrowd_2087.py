'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Dicionários
Objetivo: Solução do problema beecrowd 2087 - Conjuntos Bons e Ruins
          https://www.beecrowd.com.br/judge/pt/problems/view/2087
          
Linha de comando para executar: python3 beecrowd_2087.py

Bom caso de teste:
5
abc
ade
ababcd
ab
adefc
'''

n = int(input())

while n > 0:
   
    vocab = {}
    
    f = 0
    for _ in range(0,n):
        string = input()
        if string in vocab:
            f+=1
        else:
            vocab[string] = len(string)
    
    keys = sorted(vocab)
    n = len(vocab)
    
    ans = f
    
    for i in range(1,n):
        
        tam = min(vocab[keys[i-1]],vocab[keys[i]])
        
        same = 0
        
        for j in range(0,tam):
            if keys[i-1][j] == keys[i][j]:
                same+=1
        
        if same == tam:
            ans+=1
            break
    
    if ans == 0:
        print('Conjunto Bom')
    else:
        print('Conjunto Ruim')

    n = int(input())


