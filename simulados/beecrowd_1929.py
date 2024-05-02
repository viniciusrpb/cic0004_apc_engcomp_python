def ehTriangulo(x,y,z):

    if x+y> z and z+y > x and x+z>y:
        return True
    return False

a,b,c,d = map(int,input().split())

if ehTriangulo(a,b,c) or ehTriangulo(a,c,d) or ehTriangulo(a,b,d) or ehTriangulo(b,c,d):
    print('S')
else:
    print('N')

