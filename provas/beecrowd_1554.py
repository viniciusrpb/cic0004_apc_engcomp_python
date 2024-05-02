'''CIC0004 - Algoritmos e Programação de Computadores
   Beecrowd 1554 - Bilhar
   Prof. Dr. Vinicius Ruela Pereira Borges '''

c = int(input())

for _ in range(c):
    
	n = int(input())
	
	#Leitura da coordenada da bola branca
	b1,b2 = map(int,input().split())
	
	#Leitura da coordenada da primeira bola
	x,y = map(int,input().split())
	
	'''Calcula a distancia (sem fazer raiz) entre a bola branca
	e a primeira bola. Assuma que esse eh, por enquanto,
	a menor distancia. Armazene o indice da primeira bola como resposta'''
	dist = (b1-x)*(b1-x) + (b2-y)*(b2-y)
	ans = 1
	
	'''Agora leia as demais bolas. Para cada uma, calcule a distancia
       com a bola branca e verifique se esta eh menor do que a jah calculada.
       Em caso afirmativo, atualize a menor distancia e a resposta
	'''
	for j in range(2,n+1):
		x,y = map(int,input().split())
		temp_dist = (b1-x)*(b1-x) + (b2-y)*(b2-y)
		if temp_dist < dist:
			dist = temp_dist
			ans = j
	
	print(ans)
