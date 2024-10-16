
#Problema: dado um tempo, determinar se a pessoa dormiu bem
#Entrada
tempo = float(input())
#Saida
if tempo > 8:
  print("Você dormiu muito bem, parabéns!")
elif tempo == 8:
  print("Você dormiu o suficiente, continue assim!")
else:
  print("Você precisa de mais tempo de sono, cuide-se!")