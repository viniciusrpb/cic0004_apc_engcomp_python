'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 1103 - Alarme Despertador
   Prof. Dr. Vinicius Ruela Pereira Borges '''

h1,m1,h2,m2 = map(int,input().split())

while h1 != 0 or m1 !=0 or h2 != 0 or m2 != 0:

    # transforma tudo para minutos
    minutos_dorme = h1*60+m1
    minutos_alarme = h2*60+m2
    
    # calcula a diferenca. Se der positivo, jah temos a resposta. Se nao, o minutos_dorme estah no dia seguinte (houve virada do dia).
    ans = minutos_alarme-minutos_dorme
    
    if ans < 0:
        ans = 1440 + ans # se entrar aqui, eh porque ans eh um valor negativo devido a virada do dia

    print(ans)

    h1,m1,h2,m2 = map(int,input().split())
