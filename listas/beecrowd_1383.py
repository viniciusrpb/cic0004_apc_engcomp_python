k = int(input())

t = 1

while t <= k:

    sudoku = [[int(x) for x in input().split()] for y in range(0,9)]

    sudoku_valido = True

    for i in range(0,9):
        hist = [0]*9
        for j in range(0,9):
            pos = sudoku[i][j]-1
            hist[pos]+=1
            if hist[pos] > 1:
                sudoku_valido = False

    for j in range(0,9):
        hist = [0]*9
        for i in range(0,9):
            pos = sudoku[i][j]-1
            hist[pos]+=1
            if hist[pos] > 1:
                sudoku_valido = False

    for i in range(1,9,3):
        for j in range(1,9,3):
            hist = [0]*9
            # analise do quadrante
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    pos = sudoku[x][y]-1
                    hist[pos]+=1
                    if hist[pos] > 1:
                        sudoku_valido = False

    if sudoku_valido == True:
        print(f'Instancia {t}\nSIM\n')
    else:
        print(f'Instancia {t}\nNAO\n')

    t+=1


