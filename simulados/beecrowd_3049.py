b = int(input())
t = int(input())

felix = (b+t)*70/2
areaR = 70*160
mariza = areaR - felix 

if felix < mariza:
    print('2')
elif mariza < felix:
    print('1')
else:
    print('0')
