l = int(input())

op = input()

n=12
matriz = []

for i in range(0,n):
    lista = []
    for j in range(0,n):
        x = float(input())
        lista.append(x)
    matriz.append(lista)

soma = 0
for j in range(0,n):
    soma+=matriz[l][j]

if op == 'S':
    print(f'{soma:.1f}')
else:
    avg = soma/n
    print(f'{avg:.1f}')

