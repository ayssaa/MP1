#Problema: dado três valores, imprimir se o último está incluso nos outros

#Entrada
valor1 = int(input ())
valor2 = int(input ())
valor3 = int(input ())

#Saida
if valor1 <= valor3 <= valor2:
  print("True")
elif valor2 <= valor3 <= valor1:
  print("True")
else:
  print(False)
  