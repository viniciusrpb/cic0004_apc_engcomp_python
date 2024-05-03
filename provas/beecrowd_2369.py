'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 2369 - Conta de Água
   Prof. Dr. Vinicius Ruela Pereira Borges '''

n = int(input())

if n > 100:
    valor = (n-100)*5 + 167
elif n > 30:
    valor = (n-30)*2 + 27
elif n > 10:
    valor = (n-10) + 7
else:
    valor = 7

print(valor)
