'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges

Tópico: Dicionários
Objetivo: Solução do problema beecrowd 2242 - Huaauhahhuahau
          https://www.beecrowd.com.br/judge/pt/problems/view/2242
          
Linha de comando para executar: python3 beecrowd_2242.py'''

risada = input()

vogais = ''

for c in risada:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        vogais+=c
    
ans = 'S'
j = len(vogais)-1
for i in range(0,len(vogais)):
    if vogais[i] != vogais[j]:
        ans = 'N'
    j-=1
    
print(ans)
