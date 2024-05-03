'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2443 - Soma de Fracoes
   Prof. Dr. Vinicius Ruela Pereira Borges '''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

a,b,c,d = map(int,input().split())

baixo = b*d
cima = d*a + b*c

mdc = gcd(baixo,cima)

baixo = baixo // mdc
cima = cima // mdc

print(f'{cima} {baixo}')
