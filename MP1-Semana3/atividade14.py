#Problema: Dado numeros, verificar se eles se repetem

#Entrada
quantidade_algarismos = int(input())
algarismos = []
verificado = []
repetido = []

#Pegando os valores do PIN e armazenando numa lista "algarismos"
for i in range(quantidade_algarismos):
  pin = int(input())
  algarismos.append(pin)

#Na lista de "verificado" vao os i, caso apareça um i repetido, ele irá para a lista "repetidos"
for i in algarismos:
  if i in verificado:
    repetido.append(i)
  else:
    verificado.append(i)

#Agora eu verifico se existe um numero em "repetidos", se sim, então printo ERRO, caso contrário OK
if repetido != []:
  print("ERRO")
else:
  print("OK")
