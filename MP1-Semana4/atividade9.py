
#Problema: Dado um valor minimo, imprimir uma sobre e o total de um somatorio
#Entrada
minimo = int(input())
somatorio_total = 0

while somatorio_total < minimo:
  conjunto = int(input())
  somatorio_total += conjunto

sobra = somatorio_total - minimo

#Saida
print("minimo", minimo)
print("total", somatorio_total)
print("sobra", sobra)