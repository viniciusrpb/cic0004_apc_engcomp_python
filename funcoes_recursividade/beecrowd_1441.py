'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Recursividade (Python)
Objetivo: Solução do problema beecrowd 1441 - Hailstone Sequences
          https://www.beecrowd.com.br/judge/pt/problems/view/1441
Linha de comando para executar: python3 beecrowd_1441.py
'''

def sequence(h):
    
    if h == 1:
        return 1
    if h % 2 == 0:
        hh = h//2
    else:
        hh = 3 * h + 1
    
    return max(sequence(hh),h)
    

n = int(input())

while n > 0:    
        
    ans = sequence(n)   
    
    print(ans)
    
    n = int(input())



    

