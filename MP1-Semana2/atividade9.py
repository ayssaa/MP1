#Problema: dado uma placa, imprimir qual dia o carro não circula

#Entrada
placas = str(input())

#Saida
placa = placas[3]
if placa == "1" or placa == "2":
  print("segunda-feira")
elif placa == "3" or placa == "4":
  print("terça-feira")
elif placa == "5" or placa == "6":
  print("quarta-feira")
elif placa == "7" or placa == "8":
  print("quinta-feira")
elif placa == "9" or placa == "0":
  print("sexta-feira")