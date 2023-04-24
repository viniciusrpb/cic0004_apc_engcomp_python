n = float(input())

reais = int(n)
centavos = n - reais
centavos = int(centavos*100)

cem = reais//100
resto = reais%100

cinquenta = resto//50
resto = resto%50

print('NOTAS:')
print(f'{cem} nota(s) de R$ 100.00')
print(f'{cinquenta} nota(s) de R$ 50.00')

print('MOEDAS:')
print(f'{resto} moeda(s) de R$ 1.00')

cents50 = centavos // 50
resto = centavos % 50
print(f'{cents50} moeda(s) de R$ 0.50')

cents25 = resto // 25
resto = resto % 25
print(f'{cents25} moeda(s) de R$ 0.25')

