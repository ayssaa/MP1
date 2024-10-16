#Problema: Histograma B

#Entrada
valor = int(input())

#Saida
if valor == 0:
  print(".")
else:
  for alg in range(1):
    print(valor * "*")