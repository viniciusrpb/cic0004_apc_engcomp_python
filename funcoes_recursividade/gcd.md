# Máximo Divisor Comum - Greatest Common Divisor (Versão Recursiva)

A ideia empregada se baseia no [Algoritmo de Euclides](http://clubes.obmep.org.br/blog/sala-de-estudos-algoritmo-de-euclides-para-determinacao-de-mdc/diagramas/)

## Ideia do Algoritmo

Sejam dois números inteiros ```a``` e ```b```. O máximo divisor comum (gcd) entre ```a``` e ```b``` ```gcd(a,b)``` é igual ao gcd entre ```a-b``` e ```b```?

Por exemplo, se ```a=84``` e ```b=14```, temos que:

```
gcd(84,14) = 4

gcd(84-14,14) = gcd(70,14) = 4
```

então

```
gcd(84,14) = gcd(84-14,14) = 4
```

se subtrairmos ```b``` duas vezes de ```a```, obtendo-se ```x=a-2b``` o gcd entre ```x``` e ```b``` se altera?

```
gcd(84-2*14,14) = gcd(84-28,14) = 4
```

## Código-fonte

```
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

print(gcd(84,12))
```

## Referências


