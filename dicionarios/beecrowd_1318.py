n,m = map(int,input().split())

while n!= 0 and m!=0:
    bilhetes = {}

    for i in range(1,n+1):
        bilhetes[i] = 0

    festa = [int(x) for x in input().split()]

    for b in festa:
        bilhetes[b] += 1

    clonado = 0
    for id_bilhete in bilhetes:
        if bilhetes[id_bilhete] > 1:
            clonado+=1

    print(clonado)
    
    n,m = map(int,input().split())
