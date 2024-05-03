'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Listas
Objetivo: Solução do problema beecrowd 1743 - Máquina de Verificação Automatizada
          https://www.beecrowd.com.br/judge/pt/problems/view/1743

Linha de comando para executar: python3 beecrowd_1743.py'''

def solve(cima,baixo):
    
    for i in range(0,len(cima)):
        if cima[i] == baixo[i]:
            return 'N'
    return 'Y'

cima = [int(x) for x in input().split()]
baixo = [int(x) for x in input().split()]

ans = solve(cima,baixo)

print(ans)
