#Problema: informar uma forma de acordo com a cor recebida

#Entrada
cor = str(input ())

#Saida
if cor == "verde":
  print("retângulo")
elif cor == "amarelo":
  print("losango")
elif cor == "azul":
  print("circunferência")
elif cor == "branco":
  print("faixa")
else:
  print("não tem essa cor")