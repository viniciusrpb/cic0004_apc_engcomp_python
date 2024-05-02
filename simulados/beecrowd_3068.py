x1,y1,x2,y2 = map(int,input().split())

teste = 1
while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:

    n = int(input())

    ans = 0
    for i in range(1,n+1):
        a,b = map(int,input().split())

        if a >= x1 and a <= x2 and b <= y1 and b >= y2:
            ans+=1

    print(f'Teste {teste}\n{ans}')

    x1,y1,x2,y2 = map(int,input().split())

    teste+=1
