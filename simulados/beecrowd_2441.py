'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2441 - Janela
   Prof. Dr. Vinicius Ruela Pereira Borges '''

f1,f2,f3 = map(int,input().split())

# ordenacao crescente: f1 < f2 < f3
if f1 > f2:
    aux = f1
    f1 = f2
    f2 = aux

if f2 > f3:
    aux = f2
    f2 = f3
    f3 = aux

if f1 > f2:
    aux = f1
    f1 = f2
    f2 = aux

# calcula a sobra da folha f2 em relacao a f1, isto eh, o excesso de folha 2
sobreposicao_f1f2 = f2-f1

# calcula a sobra da folha f3 em relacao a f2, isto eh, o excesso de folha 3
sobreposicao_f2f3 = f3-f2

# inicializa o calculo da area
area = 0

# se existir sobreposicao entre folhas 1 e 2,
# deve-se calcular a "sobra" (espaco vazio) do ponto 0 até o 400
# logo, desconta-se a sobreposicao da "area" total das janelas 1 e 2 (400, no)
if sobreposicao_f1f2 <= 200:
    area = area + (200-sobreposicao_f1f2)

# analogamente, se existir sobreposicao entre folhas 2 e 3,
# deve-se calcular a "sobra" (espaco vazio) do ponto 200 até o 600

if sobreposicao_f2f3 <= 200:
    area = area + (200-sobreposicao_f2f3)

# calcula a area em cm
ans = 100*(area)

print(ans)
