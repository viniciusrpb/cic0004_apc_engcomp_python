n = int(input())

while n > 0:

    cifrada = input()
    shift = int(input())

    decifrada = ''

    for ch in cifrada:
        asci = ord(ch)-65
        asci = (asci - shift)%26
        novo_ch = chr(asci+65)
        decifrada = decifrada+novo_ch

    print(decifrada)

    n -=1
