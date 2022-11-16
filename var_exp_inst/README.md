# Exemplos de leitura e escrita de dados em Python

## Leitura

Em Python, a leitura de dados da entrada padrão é feita por meio da função [input]().

A função retorna 

![Como funciona a função input](imgs/input1.png)

### Leitura de um número em uma linha

```
value = input()
value = int(value)
```

de maneira simplificada

```
value = int(input())
```

### Leitura de um número em uma linha com pergunta

**Não utilize essa abordagem em juízes automáticos ou ambiente com correção automática, como Coderunner, Codeforces e Beecrowd**

```
value = input("Digite um numero inteiro: ")
value = int(value)
```

de maneira simplificada

```
value = int(input("Digite um numero inteiro: "))
```

### Leitura de dois números inteiros separados por espaço em branco

Estratégia 1

```
a,b = (for x in input().split())
a = int(a)
b = int(b)
```

de maneira simplificada:

```
a,b = (int(x) for x in input().split())
```

Estratégia 2

```
a,b = map(int, input().split())
```

## Escrita

### Estratégia 1: print formatado:

```
value = 1234.56234536457
print(f'Valor: {value:.3f}')
```

### Estratégia 2: método format:

```
value = 1234.56234536457
print('Valor: {:.3f}'.format(value))
```
