'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Strings
Objetivo: Solução do problema beecrowd 1024 - Criptografia
          https://www.beecrowd.com.br/judge/pt/problems/view/1024
Linha de comando para executar: python3 beecrowd_1024.py'''

def isLower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

def isUpper(c):
    if ord(c) >= 65 and ord(c) <= 90:
        return True
    else:
        return False

def solve(s):

    #procedimento 1
    s1 = ''
    for carac in s:
        if isLower(carac) == True or isUpper(carac) == True:
            asc2 = ord(carac)+3
            novo_carac = chr(asc2)
            s1+=novo_carac # s1=s1+novo_carac
        else:
            s1+=carac # s1=s1+carac

    # procedimento 2
    s2 = s1[::-1]

    #procedimento 3
    n = len(s2)
    s3 = s2[0:n//2] #substring formada pelos caracteres no intervalo [0,1,2,...,n//2)
    for i in range(n//2,n):
        caractere = s2[i]
        asc2 = ord(caractere)-1
        novo_carac = chr(asc2)
        s3=s3+novo_carac

    return s3

n = int(input())

for _ in range(0,n):

    string = input()

    ans = solve(string)

    print(ans)
