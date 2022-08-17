n = int(input())

while n:
    
    car = []
    gained = []
    start = [0]*n
    flag = True
    
    for i in range(0,n):
        c,p = (int(x) for x in input().split())
        
        car.append(c)
        gained.append(p)
    
    for i in range(0,n):
        if gained[i] == 0:
            start[i] = car[i]
        elif i+gained[i] >= 0 and i+gained[i] < n:
            start[i+gained[i]] = car[i]
    
    for i in range(0,n):
        if start[i] == 0:
            flag = False
    
    if flag == False:
        ans='-1'
    else:
        ans = ''
        for i in range(0,n-1):
            ans+=str(start[i])+" "
        ans+=str(start[n-1])
    
    print(ans)
    n = int(input())
