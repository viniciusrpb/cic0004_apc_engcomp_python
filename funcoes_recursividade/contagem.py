def contagem(a):
    if a >= 0:
        print(a)
        contagem(a-1)

n = input()
n = int(n)

contagem(n)
