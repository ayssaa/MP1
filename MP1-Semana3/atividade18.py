#Problema: Newton

#Entrada
massa = float(input())
num_voltas = int(input())
melhor_aceleracao = 0
melhor_volta = 0

#Achando minhas variaveis
for volta in range(num_voltas):
  forca = float(input()) # força em cada volta
  aceleracao = forca / massa
  if aceleracao > melhor_aceleracao:
    melhor_aceleracao = aceleracao
    melhor_volta = volta + 1

#Saida
print("melhor_volta:", melhor_volta)
print("maior aceleração:", "%.1f" % melhor_aceleracao)
