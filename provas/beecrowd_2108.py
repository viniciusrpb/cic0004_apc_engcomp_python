'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Strings
Objetivo: Solução do problema beecrowd 2108 - Contando Caracters
          https://beecrowd.com.br/judge/pt/problems/view/2108

Linha de comando para executar: python3 beecrowd_2108.py'''

string = input()
maior = -1
mt = ''

while string != '0':

    ans = ''

    for token in string.split():
        ans+=str(len(token))+'-'

    if len(token) > maior:
        mt = token
        maior = len(token)

    print(ans[:-1])
    string = input()

print()
print(f'The biggest word: {mt}')
