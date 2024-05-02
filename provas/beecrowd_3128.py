'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 3128 - Regras do Cinema
   Prof. Dr. Vinicius Ruela Pereira Borges '''

x = int(input())
y = int(input())

if x >= 6 and y >=6 and ((x >= 18 or y >= 18) or (x>=14 and y >= 14)):
    print('YES')
else:
    print('NO')

