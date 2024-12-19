#Problema: Dados V ou F, imprimir uma resposta

#Entrada
valor1 = str(input())
valor2 = str(input())

#Saida
if valor1 == valor2 and valor1 == "V":
  print("VV")
elif valor1 == valor2 and valor1 == "F":
  print("FF")
else:
  print("?")
  