def ordenacao(v,n):

    trocas=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                aux = v[j]
                v[j] = v[i]
                v[i] = aux
                trocas+=1

    return trocas

lista = [1,2,2,3,2]

n = len(lista)

print(lista) # imprime a lista antes da ordenacao

ans = ordenacao(lista,n)

print(ans) # imprimir a quantidade de trocas
print(lista) # imprimir a lista apos ordenacao
