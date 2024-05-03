while True:
	
	try:
	
		n = int(input())
		
		part1 = n//3
		
		for i in range(0,n):
		
			linha = ''
			for j in range(0,n):
				
				aij = 0
				
				if i == j:
					aij = 2
				
				if n-j-1 == i:
					aij = 3
				
				if i >= part1 and i <= n-1-part1 and j >= part1 and j <= n-1-part1:
					if i == n//2 and j == n//2:
						aij = 4
					else:
						aij = 1
				
				linha+=str(aij)
		
			print(linha)
		
		print()
	
	except EOFError:
		break
