n = int(input())

fib = [1]

if n > 1:
    fib.append(1)

for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])

#print(*fib[::-1],sep=' ')

ans = ''
for i in range(len(fib)-1,0,-1):
    ans = ans+str(fib[i])+" "
ans = ans+str(fib[0])
print(ans)
