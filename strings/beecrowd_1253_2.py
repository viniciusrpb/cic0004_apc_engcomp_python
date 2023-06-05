n = int(input())

while n > 0:

    cifrada = input()
    m = int(input())
    original = ''

    for caractere in cifrada:

        cod_ascii = ord(caractere)
        cod_ascii -= 65

        if cod_ascii - m < 0:
            cod_ascii = cod_ascii + 26 - m
        else:
            cod_ascii = cod_ascii - m

        original += chr(cod_ascii+65)

    print(original)

    n-=1
