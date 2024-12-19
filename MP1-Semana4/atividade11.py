#Problema: Verificar quantas taxas atuais de desmatamento foram abaixo de uma taxa definida

#Entrada
pior_taxa = float(input())
contagem_melhores_taxas = 0
contagem_total = 0

while True:
  taxa_atual = float(input())
  if taxa_atual < 0:
    break
  contagem_total += 1
  if taxa_atual < pior_taxa:
    contagem_melhores_taxas += 1


#Saida
print(contagem_total, contagem_melhores_taxas)
