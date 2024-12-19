#Problema: Civis e militares

#Entrada
baixas = int(input())
civil = 0
militar = 0

#Saida
for num in range(baixas):
  tipo = str(input())
  if tipo == "Civil":
    civil += 1
  else:
    militar += 1
print("civis mortos", civil)
print("militares mortos", militar)
