#Problema: Dado um valor decimal, mostrar com 2, 4, 6, 8 e 10 casas decimais.

# Entrada
valorp = float(input())  # número decimal

# Imprimir resultado
print("%.2f" % valorp)
print("%.4f" % valorp)
print("%.6f" % valorp)
print("%.8f" % valorp)
print("%.10f" % valorp)
