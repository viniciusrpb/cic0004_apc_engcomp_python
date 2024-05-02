'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2428 - Capital
   Prof. Dr. Vinicius Ruela Pereira Borges '''

a1,a2,a3,a4 = map(int,input().split())

if a1*a2 == a3*a4 or a1*a4 == a2*a3 or a1*a3 == a2*a4:
    print('S')
else:
    print('N')
