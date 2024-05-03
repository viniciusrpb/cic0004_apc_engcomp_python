while True:

    try:
        n,m = (int(x) for x in input().split())

        matriz = [[0]*(m+2)]

        for i in range(1,n+1):
            lista = [0]
            aux = [int(x) for x in input().split()]
            for x in aux:
                lista.append(x)
            lista.append(0)
            matriz.append(lista)

        matriz.append([0]*(m+2))

        for i in range(1,n+1):
            s = ''
            for j in range(1,m+1):
                if matriz[i][j] == 1:
                    s+='9'
                else:
                    soma = matriz[i+1][j]+matriz[i-1][j]+matriz[i][j-1]+matriz[i][j+1]
                    s+=str(soma)
            print(s)
    except EOFError:
        break
