#Problema: Juros Composto

#Entrada
valori = float(input ())
taxa = float(input ())

#Calculando cada juros
periodo1 = (valori * taxa) + valori
periodo2 = (periodo1 * taxa) + periodo1
periodo3 = (periodo2 * taxa) + periodo2

#Valores
print("%.2f" % periodo1)
print("%.2f" % periodo2)
print("%.2f" % periodo3)
