#Problema: Newton... De novo!?!?

#Entrada e variaveis
massa = float(input())
aceleracao_inicial = float(input())
aceleracao = [aceleracao_inicial]
numero_voltas = 0
forca = 1

#Calculando as aceleracoes de cada volta
while forca >= 0:
  forca = float(input())
  numero_voltas += 1
  aceleracao.append(forca / massa)

#Achando qual foi a maior aceleracao da lista de aceleracoes por voltas
aceleracao_maxima = max(aceleracao)

#Saida
print("maior aceleração:", "%.3f" % aceleracao_maxima)
print("número de voltas: ", numero_voltas)
