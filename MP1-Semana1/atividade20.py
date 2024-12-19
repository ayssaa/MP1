#Problema: Newton

#Entrada
massa = float(input ()) #massa em kg
forca = float(input ()) #força em N

#Calculando a aceleração em metros por segundo ao quadrado
a = forca / massa

#Valores
print("aceleração= " + str("%.1f" % a))
