#Problema: Dado uma taxa, imprimir quais sao maiores que a pior taxa definida

#Entrada
pior_estimativa = float(input())
numero_ocorrencias = int(input())
quantas_superam = 0
for i in range(numero_ocorrencias):
  taxa = float(input())
  if taxa > pior_estimativa:
    quantas_superam += 1
    
#Saida
print(quantas_superam)
