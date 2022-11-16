# Exemplos de leitura e escrita de dados em Python

## Leitura

Em Python, a leitura de dados da entrada padrão é feita por meio da função [input](https://docs.python.org/3/tutorial/inputoutput.html). Essa função captura todos os caracteres que foram digitados em uma linha fornecida na entrada. Define-se que uma linha da entrada é toda a sequência de caracteres que é digitada até que se aperte a tecla *ENTER* ou quando se está lendo um arquivo e o caractere ```\n``` é encontrado.

A função ```input()``` retorna uma string, isto é, uma sentença que também pode ser vista como uma cadeia de caracteres. Normalmente, a leitura da entrada **depende** do problema a ser resolvido. Assim, é comum utilizar o método ```split()``` na string obtida após o método ```input()``` para separar cada termo que é interessante para o nosso problema. A Figura abaixo ilusta essa ideia:

![Como funciona a função input](imgs/input1.png)

Vamos agora analisar alguns casos de leitura de entrada que são comumente encontrados na resolução de problemas:

### Leitura de uma frase em uma linha na entrada

```
frase = input()
```

### Leitura de duas palavras da entrada, uma em cada linha 

```
word1 = input()
word2 = input()
```

### Leitura de duas palavras da entrada separadas por espaço em branco, na mesma linha 

```
word1,word2 = (for x in input().split())
```

### Leitura de duas palavras da entrada separadas por vírgula, na mesma linha 

```
word1,word2 = (for x in input().split(','))
```

### Leitura de um número inteiro em uma linha

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
a,b = (x for x in input().split())
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

### Leitura de três números inteiros separados por espaço em branco, na mesma linha

Estratégia 1

```
a,b,c = (int(x) for x in input().split())
```

Estratégia 2

```
a,b,c = map(int, input().split())
```

### Leitura de dois números inteiros e uma palavra (nessa ordem) separados por espaço em branco, na mesma linha


```
a,b,word = (x for x in input().split())
a = int(a)
b = int(b)
```

Observe que apenas ```a``` e ```b``` são convertidos para inteiros, já que word é naturalmente uma string


### Leitura de um número real, um número inteiro e uma palavra (nessa ordem) separados por espaço em branco, na mesma linha


```
real,inteiro,word = (x for x in input().split())
real = float(real)
inteiro = int(inteiro)
```

Observe que apenas ```a``` e ```b``` são convertidos para inteiros, já que word é naturalmente uma string


## Escrita

### Escrita de um número inteiro

Estratégia 1 

```
value = 1234
print(f'Valor: {value}')
```

Estratégia 2: método format

```
value = 1234
print('Valor: {:d}'.format(value))
```

### Escrita de um número real com três casas decimais de precisão

Estratégia 1 

```
value = 1234.56234536457
print(f'Valor: {value:.3f}')
```

Estratégia 2: método format

```
value = 1234.56234536457
print('Valor: {:.3f}'.format(value))
```

### Escrita de um número inteiro com exatamente 7 digitos inteiros à esquerda

Espaçamento em branco

```
value = 1234
print(f'Valor: {value:7d}')
```

Com zeros à esquerda

```
value = 1234
print(f'Valor: {value:07d}')
```

### Escrita de dois números inteiros em linhas separadas

Estratégia 1

```
a = 3
b = 5
print(a)
print(b)
```

Estratégia 2


```
a = 3
b = 5
print(f'{a}\n{b}')
```

### Escrita de dois números inteiros separados por espaço em branco

```
a = 3
b = 5
print(f'{a} {b}')
```

## Referências

- [Documentação do Python](https://docs.python.org/3/tutorial/inputoutput.html)

- [Material IME/USP](https://panda.ime.usp.br/panda/static/pythonds_pt/01-Introducao/09-entradaSaida.html)
