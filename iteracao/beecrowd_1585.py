def areaLosango(d1,d2):
  return (d1*d2)/2.0

n = int(input())

while n > 0:
  x,y = input().split()
  x = float(x)
  y = float(y)
  ans = areaLosango(x,y)
  print(f'{int(ans)} cm2')
  n -= 1
