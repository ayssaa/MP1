#Problema: Descobrir quanto de memoria esse codigo usa!
#Entrada
memoria_utilizada = 0
maior_memoria_utilizada = []

while True:
  memoria = int(input())
  memoria_utilizada += memoria
  maior_memoria_utilizada.append(memoria_utilizada)
  if memoria == 0:
    break

#Saida
print(max(maior_memoria_utilizada))