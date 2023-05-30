n = int(input())

while n != 0:

    for i in range(1,n+1):
        linha = ''
        for j in range(1,n+1):
            if i > j:
                a = str(i-j+1)
            else:
                a = str(j-i+1)

            esp = ' '*(3-len(a))

            linha+=esp+str(a)+" "
        print(linha[:-1])
    print()

    n = int(input())
