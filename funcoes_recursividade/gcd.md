# Máximo Divisor Comum - Greatest Common Divisor (Versão Recursiva)

A ideia empregada para o cálculo do Máximo Divisor Comum (*Greatest Common Divisor* - GCD) se baseia no [Algoritmo de Euclides](http://clubes.obmep.org.br/blog/sala-de-estudos-algoritmo-de-euclides-para-determinacao-de-mdc/diagramas/).

## Definição

O GCD entre dois números inteiros positivos é o maior divisor em comum entre eles. Por exemplo, se ```a=84``` e ```b=16```, podemos ver pela fatoração de cada número pelos seus fatores primos que:

```
84 = ** 2 x 2 ** x 3 x 7

16 = ** 2 x 2 ** x 2 x 2
```

Podemos ver que existe uma sequência de ```2x2``` em comum na fatoração de 84 e 16. Logo o GCD entre 84 e 16 é 2 x 2 = 4.

Por definição, temos que:

```
gcd(a,0) = a
```

## Ideia do Algoritmo

Sejam dois números inteiros ```a``` e ```b```, em que ```a > b```. O máximo divisor comum (gcd) entre ```a``` e ```b``` ```gcd(a,b)``` é igual ao gcd entre ```a-b``` e ```b```?

Por exemplo, se ```a=84``` e ```b=16```, sabemos no exemplo acima que o ```gcd(84,16) = 4```. Como ficaria o GCD entre ```84-16=68``` e ```16```?

```
68 = 2 x 2 x 17
16 = 2 x 2 x 2 x 2
```

Podemos verificar que o GCD entre 68 e 16 também é ```4```. E agora, se subtrairmos ```b``` duas vezes de ```a```, obtendo-se ```x=a-2b``` o gcd entre ```x``` e ```b``` se altera? Bom, ```x = a - 2b = 84 - 32 = 52```, então:

```
52 = 2 x 2 x 13
16 = 2 x 2 x 2 x 2
```

O GCD entre 52 e 16 também é ```4```. Por fim, vamos subtrair ```b``` três vezes de ```a```, obtendo-se ```x=a-3b```. Agora, o gcd entre ```x``` e ```b``` será 4? Fazendo-se ```x = a - 3b = 84 - 48 = 36```, então:

```
36 = 2 x 2 x 9
16 = 2 x 2 x 2 x 2
```

E também o GCD entre ```a-3b``` e ```b``` também é 4! Podemos então formular que:

```
gcd(a,b) = gcd(a-b,b) = gcd(a-2b,b) = gcd(a-3b,b) = ... = gcd(a-yb,b)
```

em que ```y``` é a quantidade de vezes que podemos subtrair ```b``` de ```a``` mantendo-se a igualdade acima. Isso mostra que não perdemos o maior divisor comum ao fazermos essas subtrações. Entretanto, chega um momento em que ```a-yb``` fica menor do que ```b```. Por exemplo, para ```y=5```, teríamos ```a-yb = 84 - 5 x 16 = 84 - 80```.

A pergunta que fica é: quantas vezes podemos subtrair ```b``` de ```a```, ou ainda, qual é o valor de  ```y```?

Resposta:
```y = a / b    (divisão inteira)```

Logo, temos que:

```
y = 84/16 = 5
```

Isso significa que:

```
gcd(84,16) = gcd(84-5*16,16) = gcd(4,16)
```

Assim, fazemos todas as substrações de uma única só vez. Como nenhum divisor pode ser maior que o número que ele divide (com exceção do zero), temos que inverter




```
gcd(a,b) = gcd(a-b, b) se a>b
```

## Código-fonte

```
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(84,16))
```

## Referências


