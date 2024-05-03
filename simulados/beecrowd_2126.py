idx = 1
while True:
    
    try:
        
        string_a = input()
        string_b = input()
        
        n = len(string_a)
        m = len(string_b)
        
        ans = 0 
        last = 0
        
        for i in range(0,m):
            
            y = i
            tam = 0
            x = 0
            
            while x < n and y < m and string_a[x] == string_b[y]:
                tam +=1
                x+=1
                y+=1
                
            if tam == n:
                ans+=1
                last = y-tam
        
        print(f'Caso #{idx}:')
        if ans > 0:
            print(f'Qtd.Subsequencias: {ans}')
            print(f'Pos: {last+1}\n')
        else:
            print(f'Nao existe subsequencia\n')
        
        idx+=1
    
    except EOFError:
        break
