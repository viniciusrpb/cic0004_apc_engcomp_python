n = int(input())

lista_par = []
lista_impar = []

for i in range(0,n):
    a = int(input())

    if a % 2 == 0:
        lista_par.append(a)
    else:
        lista_impar.append(a)

lista_par.sort()
lista_impar.sort(reverse=True)

for elem in lista_par:
    print(elem)

for elem in lista_impar:
    print(elem)










