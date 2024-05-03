def ehMinusculo(carac):
    if ord(carac) > 96:
        return True
    return False

c = int(input())

while c > 0:

    string = input()
    hidden = ''

    for ch in string[::-1]:
        if ehMinusculo(ch) == True:
            hidden=hidden+ch

    print(hidden)

    c-=1
