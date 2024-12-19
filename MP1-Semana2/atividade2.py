#Problema: dado dois valores, dizer se o saldo é suficiente ou não

#Entrada
valorb = int(input ()) #valor do banco
totalc = int(input ()) #total do carrinho

#Saida
if valorb >= totalc:
  print("pode comprar tudo")
else:
  print("saldo insuficiente")
  