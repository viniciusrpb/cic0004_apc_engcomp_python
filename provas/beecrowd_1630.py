'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 1630 - Estacas
   Prof. Dr. Vinicius Ruela Pereira Borges '''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

while True:
    try:
        x,y = map(int,input().split())
        
        ans = 2*(x+y)//gcd(x,y)
        
        print(ans)
    except EOFError:
        break
