r = int(input())

n = 1

while r > 0:

  aldo = 0
  beto = 0
  print("Teste "+str(n))

  while r > 0:
    a,b = input().split()
    a = int(a)
    b = int(b)

    aldo=aldo+a
    beto=beto+b

    r=r-1

  if aldo > beto:
    print("Aldo\n")
  else:
    print("Beto\n")

  r = int(input())
  n=n+1
  
