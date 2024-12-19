#Problema: dado uma letra, responder uma direção

#Entrada
letra = str(input ()) 

#Saida
if letra == "w" or letra == "W":
  print("UP")
elif letra == "a" or letra == "A":
  print("LEFT")
elif letra == "s" or letra == "S":
  print("DOWN")
elif letra == "d" or letra == "D":
  print("RIGHT")
else:
  print("?")
  