#Prova: Dolar 3
#Entrada
periodo = int(input())
taxas = []

for i in range(periodo):
  taxa = float(input())
  taxas.append(taxa)

maior_taxa = max(taxas)
menor_taxa = min(taxas)

#Saida
print("%.2f" % maior_taxa)
print("%.2f" % menor_taxa)