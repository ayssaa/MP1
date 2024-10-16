#Problema: Dado um caractere qual sua classificacao
#Entrada
caractere = str(input())
#Saida
vogal = ["A","a","E","e","I","i","O","o","U","u"]
algarismo = ["0","1","2","3","4","5","6","7","8","9"]
especial = ["@","#","$","%","&","*","(",")","_","+","-","=","!"]
if caractere in vogal:
  print("vogal")
elif caractere in algarismo:
  print("algarismo")
elif caractere in especial:
  print("especial")
else:
  print("outro")