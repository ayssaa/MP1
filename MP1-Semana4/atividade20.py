
#Problema: Calorias
#Entrada
calorias_recomendadas = int(input())
calorias_consumidas = 0

while calorias_consumidas < calorias_recomendadas:
  caloria = int(input())
  if calorias_consumidas <= calorias_recomendadas:
    calorias_consumidas = calorias_consumidas + caloria

#Saida
print("total:", calorias_consumidas)