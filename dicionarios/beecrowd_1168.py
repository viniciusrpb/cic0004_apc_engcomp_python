dicionario = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

n = int(input())

while n > 0:

    string = input()

    ans = 0
    for c in string:
        ans+= dicionario[c]

    print(f'{ans} leds')

    n-=1
