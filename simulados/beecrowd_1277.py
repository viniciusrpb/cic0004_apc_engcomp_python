t = int(input())

while t > 0:
    
    n = int(input())
    
    students = input()
    
    frequencia = input()
    k = len(frequencia)
    l = len(students)
    i = 0
    total=0
    ans = ''
    s = 0
    
    for j in range(0,n):
        
        student = ''
        while s < l and students[s] != ' ':
            student+=students[s]
            s+=1
        
        a = 0
        p = 0
        
        while i < k and frequencia[i] != ' ':
            
            if frequencia[i] == 'A':
                a+=1
            elif frequencia[i] == 'P':
                p+=1
                
            i+=1
        
        if p/(a+p) < 0.75:
            ans+=student+" "
            total+=1
            
        s+=1    
        i+=1
        
    if total > 0:
        print(ans[:-1])
    else:
        print()
    
    t-=1
