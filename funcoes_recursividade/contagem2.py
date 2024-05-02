def ehPar(w):
    if w % 2 == 0:
        return True
    else:
        return False

def contagem(a):
    if a >= 0:
        if ehPar(a) == True:
            contagem(a-2)
        else:
            contagem(a-1)
        print(a)


n = input()
n = int(n)

contagem(n)
