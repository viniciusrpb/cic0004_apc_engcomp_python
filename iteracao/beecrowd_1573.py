a,b,c = (float(x) for x in input().split(" "))

while a > 0 and b > 0 and c > 0:

    x = a*b*c;
    ans = int(x**(1./3))

    print(int(ans))

    a,b,c = (int(x) for x in input().split(" "))

