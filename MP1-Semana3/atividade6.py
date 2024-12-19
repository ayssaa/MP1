#Problema: Dado três valores, imprimir tabuada

#Entrada
tabuada = int(input())
primeiro = int(input())
ultimo = int(input())

#Saida
print("Tabuada do", tabuada, "de", primeiro, "até", ultimo)
for alg in range(primeiro, ultimo + 1):
  print(tabuada, "x", alg, "=", alg * tabuada)
  