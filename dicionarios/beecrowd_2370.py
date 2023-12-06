# ATENCAO: Codigo-fonte incompleto!

n,k = map(int,input().split())

jogadores = {}

for i in range(n):
    nome,habilidade = input().split()
    habilidade = int(habilidade)
    jogadores[habilidade] = nome

times = {}
for i in range(1,k+1):
    times[i] = []

#jogadores eh uma lista contendo apenas as chaves ordenadas decrescente
habilidades_ordenadas = sorted(jogadores)

id_time = 1
# pega cada habilidade em ordem decrescente
for habilidade in habilidades_ordenadas:
    #pega o nome do jogador associado a habilidade
    nome = jogadores[habilidade]

    #coloca o nome do jogador na chave id_time do dicionario de times
    times[id_time].append(nome)
    id_time+=1
    if id_time == k+1:
        id_time = 1

for time in times:
    print(f'Time {time}')
    # ordena a lista dos jogadores do "time" de maneira alfabetica no dicionario
    times[time].sort()
    for nome_jogador in times[time]:
        print(nome_jogador)
    print()
