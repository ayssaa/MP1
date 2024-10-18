#Problema: programa comilao :D
#Entrada
parada = str(input())
contador_linhas = 0

while True:
  entrada = str(input())
  if entrada != parada:
    contador_linhas += 1
  else:
    break

#Saida
print(contador_linhas)  