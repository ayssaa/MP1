#Problema: Dados dois pontos no espaço, qual a distância entre eles

#Entrada
x1 , y1 = [int(i) for i in input().split()] 
x2 , y2 = [int(i) for i in input().split()] 

#Continha
dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

#Saida
print("%.1f" % dist)
