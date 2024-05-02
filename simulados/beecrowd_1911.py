'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 1911 - Ajude Girafales
          https://www.beecrowd.com.br/judge/pt/problems/view/1911
          
Linha de comando para executar: python3 beecrowd_1911.py
'''

def diferenca(string1,string2):
    
    ans = 0
    
    maior1 = len(string1);
    maior2 = len(string2);
    menor = min(maior1,maior2);
    maior = min(maior1,maior2);
    
    for i in range(0,menor):
        if string1[i] != string2[i]:
            ans+=1
    
    return ans+(maior-menor)

n = int(input())

while n:
    
    assinatura = {}
    
    for i in range(n):
        nome,assin = input().split()
        assinatura[nome]=assin

    m = int(input())

    ans = 0

    for i in range(m):
        aluno,assin = input().split()
        ans += (diferenca(assinatura[aluno],assin)>1)

    print(ans)
    
    n = int(input())
