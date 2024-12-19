#Problema: dado dois valores, dizer se o saldo é suficiente ou não

#Entrada
valorb = int(input ()) #valor do banco
totalc = int(input ()) #total do carrinho

#Saida
if valorb >= totalc:
  saldo = valorb - totalc
  print("se você comprar tudo o saldo será:", saldo)
else:
  print("seu saldo é insuficiente para essa compra")
  