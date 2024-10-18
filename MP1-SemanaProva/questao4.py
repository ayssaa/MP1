#Prova: Dolar 4
#Entrada
lista_taxas = []

while True:
  taxa = float(input())
  lista_taxas.append(taxa)
  maior_taxa = max(lista_taxas)
  if taxa < maior_taxa:
    break

#Saida
print(maior_taxa)