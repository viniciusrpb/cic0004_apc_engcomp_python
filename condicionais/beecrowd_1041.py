''' recursao '''

def f(n):
    # caso base: parada da recursao
    if n >= 0:
        f(n-1)
        print(n)

f(6)

