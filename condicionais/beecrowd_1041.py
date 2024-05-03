x,y = input().split()
x = float(x)
y = float(y)

if x == 0 and y == 0:
    print('Origem')
elif x != 0 and y == 0:
    print('Eixo X')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y > 0:
    print('Q2')
else:
    print('Q3')

