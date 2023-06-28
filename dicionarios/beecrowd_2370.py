# ATENCAO: Codigo-fonte incompleto!

n,k = map(int,input().split())

jogadores = {}

for i in range(n):
    nome,habilidade = input().split()
    habilidade = int(habilidade)
    jogadores[habilidade] = nome

times = {}

#jogadores eh um dicionario ordenado
# de maneira decrescente de acordo com
# as habilidades dos jogadores
t = 1
for jogador in sorted(jogadores):
    if t in times:
        times[t].append(jogadores[jogador])
    else:
        times[t] = [jogadores[jogador]]
    t+=1
    if t == k+1:
        t=1

# ordena a lista dos jogadores do time de maneira alfabetica
for t in times:
    times[t].sort()

