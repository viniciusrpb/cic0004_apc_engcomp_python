'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2286 - Par ou Ímpar
   Prof. Dr. Vinicius Ruela Pereira Borges '''

n = int(input())

teste=1
while n != 0:
    nome1 = input()
    nome2 = input()
    
    print(f'Teste {teste}')
    for _ in range(1,n+1):
        a,b = map(int,input().split())
        
        if (a+b)%2  == 0:
            print(nome1)
        else:
            print(nome2)
    
    print()
    n = int(input())
    teste+=1
