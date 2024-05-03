'''
Universidade de Brasília
Departamento de Ciência da Computação
CIC0004 - Algoritmos e Programação de Computadores
Prof. Dr. Vinícius R. P. Borges
Tópico: Funcoes
Objetivo: Solução do problema beecrowd 1021 - Notas e Moedas
          https://www.beecrowd.com.br/judge/pt/problems/view/1021
Linha de comando para executar: python3 beecrowd_1021.py '''

def notas(grana,valor):
    
    quant_valor = grana // valor
    resto = grana % valor
    
    print(f'{quant_valor} nota(s) de R$ {valor:.2f}')
    
    return resto
    
def moedas(grana,valor):
    
    valor2 = round(valor*100.00)
    quant_valor = grana // valor2
    resto = grana % valor2
    
    print(f'{quant_valor} moeda(s) de R$ {valor:.2f}')
    
    return resto

n = float(input())

reais = int(n)
centavos = n - reais
centavos = round(centavos*100)

print('NOTAS:')
sobra = notas(reais,100)
sobra = notas(sobra,50)
sobra = notas(sobra,20)
sobra = notas(sobra,10)
sobra = notas(sobra,5)
sobra = notas(sobra,2)

print('MOEDAS:')
sobra = moedas(sobra*100,1.00)
sobra = moedas(centavos,0.50)
sobra = moedas(sobra,0.25)
sobra = moedas(sobra,0.10)
sobra = moedas(sobra,0.05)
sobra = moedas(sobra,0.01)
