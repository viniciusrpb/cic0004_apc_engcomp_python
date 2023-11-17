'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2373 - Garcom
   Prof. Dr. Vinicius Ruela Pereira Borges '''

n = int(input())

ans = 0
for _ in range(0,n):
    l,c = map(int,input().split())
    
    if l > c:
        ans+=c
        
print(ans)
