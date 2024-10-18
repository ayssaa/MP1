
#Problema: Dado uma resposta do sensor, informar se um usuário está ativo ou sedentário
#Entrada
parado = 1
movimento = 0
sensor = ""

while sensor != "f":
  sensor = str(input())
  if sensor == "m":
    movimento += 1
  elif sensor == "p":
    parado += 1

#Saida
if movimento > parado:
  print("ativo")
else:
  print("sedentário")