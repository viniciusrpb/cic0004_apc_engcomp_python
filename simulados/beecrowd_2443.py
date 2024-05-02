a,b,c,d = map(int,input().split())

den = b*d

num = a*(den//b) + c*(den//d)

for i in range(2,b*d+1):
    
    while num > 1 and num % i == 0 and den % i == 0:
        num = num // i
        den = den // i

print(f'{num} {den}')
