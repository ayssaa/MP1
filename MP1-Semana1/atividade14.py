
#Problema: Gorjeta

# Entrada
conta = float(input ())
porcentagem = int(input ()) / 100 # porcentagem que o cliente quer

# Calculando o valor final
valorfinal = (conta* porcentagem) + conta

# preço total
print("%.2f" % valorfinal)