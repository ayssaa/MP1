#Problema: Dado um valor de 1 a 11, imprimir tabuada

#Entrada
valor = int(input())

#Saida
print("Tabuada do", valor)
for alg in range(1,12):
  print(valor, "x", alg, "=", alg * valor)